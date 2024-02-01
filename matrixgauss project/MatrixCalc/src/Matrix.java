//

class Matrix {
  int rows,cols;
  int dsign = 1;

  Fraction a[][];

  Matrix(String s) {
    if(s.length()>0) 
      if ( s.charAt(s.length()-1)!= '\n') s+= '\n';
    int c = 0;
    int k = s.indexOf('\n');
    while( k!=-1 ) {
      c++;
      k = s.indexOf('\n',k+1);
    }
    this.rows = c;
    c = 1;
    k = s.indexOf('\n');
    int x = s.indexOf(' ');
    while( x!=-1 && x<k ) {
      c++;
      x = s.indexOf(' ',x+1);
    }
    this.cols = c;
    if(this.cols==0 || this.rows==0) {
      this.cols=0;
      this.rows=0;
    }
    s = s.replace('\n',' ');
    x = 0;
    a = new Fraction [this.rows][this.cols];
    for(int i = 0;i<this.rows;i++)
      for(int j = 0;j<this.cols;j++) {
        a[i][j] = new Fraction( s.substring(x,s.indexOf(' ',x)) );
        x = s.indexOf(' ',x)+1;
      }

  }
  Matrix(int rws,int cls) {
    this.rows = rws;
    this.cols = cls; 
    a = new Fraction [this.rows][this.cols];
    for(int i = 0;i<this.rows;i++)
      for(int j = 0;j<this.cols;j++)
        a[i][j] = new Fraction(0);
  }
  Matrix(int e,int rws,int cls) {
   //e = 1 - unitary matrix;
    this.rows = rws;
    this.cols = cls; 
    a = new Fraction [this.rows][this.cols];
    for(int i = 0;i<this.rows;i++)
      for(int j = 0;j<this.cols;j++)
        a[i][j] = (i==j?new Fraction(1):new Fraction(0));
  }

  public String toString() {
    String s = "";
    for(int i = 0;i<this.rows;i++) {
      for(int j = 0;j<this.cols;j++)
        s += a[i][j]+(j!=this.cols-1?" \t":"\n");
    }
    return s;
  }

  Matrix getAugmented(Matrix m) {
    Matrix n = new Matrix(this.rows,this.cols+m.cols);
    for(int i=0;i<n.rows;i++)
      for(int j=0;j<n.cols;j++)
        n.a[i][j] = (j<this.cols?this.a[i][j].getcopy():m.a[i][j-this.cols].getcopy());
    return n;
  }

// .getcopy() ????????????????????????????
void swapCols(int i,int j) { // i <-> j
 Fraction t;
 for(int k=0;k<this.rows;k++) {
  t = this.a[k][i].getcopy();
  this.a[k][i] = this.a[k][j].getcopy();
  this.a[k][j] = t.getcopy();
 }
}

void swapRows(int i,int j) { // i <-> j
 Fraction t;
 for(int k=0;k<this.cols;k++) {
  t = this.a[i][k].getcopy();
  this.a[i][k] = this.a[j][k].getcopy();
  this.a[j][k] = t.getcopy();
 }
}

Matrix getcopy() {
  Matrix m = new Matrix(this.rows,this.cols);
  for(int i=0;i<this.rows;i++)
    for(int j=0;j<this.cols;j++)
      m.a[i][j] = this.a[i][j].getcopy();
  return m;
}

Matrix getEchelon(int canswapcols) {
 Matrix m = this.getcopy();
 int j,k,l,last=m.cols-1;
 int z = Math.min(m.rows,m.cols);
 for(int i=0;i<z;i++) {
  k= i;
  while (k!=m.rows && m.a[k][i].cmp(0)==0) { //ищем ненулевой элемент в столбце i
   k++;
   if (k==m.rows) {
    if (last <= i)
      break;
    else
	   if (canswapcols!=0) {
        //если в столбце все нули, то меняем его с последним...
        m.swapCols(i,last);
        last--; // last - последний столбец, в котором возможно есть один != 0
        k = i;
      }
   }
  }
  
  if (k!=i && k!=m.rows) { // переставляем строчки!
   m.swapRows(k,i);
   m.dsign = -m.dsign; // нужно передавать для определителя! 
  }
  if (k!=m.rows)
   for (j= 0;j<m.rows;j++) {  //обнуляем строки ниже диагонали //начинаем с 0, чтобы обнулить все, кроме диагонали!
    if (j==i) continue;
     for (l=i+1;l<m.cols;l++)
       m.a[j][l] = m.a[j][l].plus( m.a[j][i].minus().divide(m.a[i][i]).times(m.a[i][l]) );
     m.a[j][i] = new Fraction(0,1);
   }
 }
 return m;
}

  Fraction getDeterminant() {
    if (this.rows != this.cols) {
      //alert(text_cant_getdet);
      return null;
    }
    Matrix m = this.getEchelon(0);
    Fraction p = new Fraction(m.dsign,1);
    for(int i=0;i<m.cols;i++)
      p = p.times(m.a[i][i]);
    return p;
  }

  Matrix getInverse() {
    Matrix ed = new Matrix(1,this.rows,this.rows);
    Matrix m  = this.getAugmented( ed );
    Matrix m1 = m.getEchelon(0);
    int i,j;
    Fraction t;
    for(i=0;i<m1.rows;i++) {
      t = m1.a[i][i].getcopy();
      if (t.cmp(0)!=0) {
        for(j=0;j<m1.cols;j++)  //делим строчку на t
          m1.a[i][j] = m1.a[i][j].divide(t);
      }else{
        // Опред = 0! Обратная не сущ.!
        // alert(text_cant_getinverse);
        return null;
      }	  
    }
    // "отделяем вторую половину"
    Matrix m2 = new Matrix(this.rows,this.cols);
    for(i=0;i<this.rows;i++)
      for(j=0;j<this.cols;j++)
        m2.a[i][j]= m1.a[i][j+this.cols].getcopy();
    return m2;
  }

  Matrix times(Matrix m) {
   if(this.cols != m.rows)
     return null;
   Matrix c = new Matrix(this.rows,m.cols);
   Fraction x;
   for(int i=0;i<c.rows;i++)
    for(int j=0;j<c.cols;j++) {
      x = new Fraction(0);
      for(int k=0;k<this.cols;k++)
        x = x.plus( this.a[i][k].times(m.a[k][j]) );
      c.a[i][j] = new Fraction(x);
    }
   return c;
  }

  Matrix plus(Matrix m,int k) {
    if(this.cols != m.cols || this.rows != m.rows)
      return null;
    Matrix c = new Matrix(this.rows,this.cols);
    for(int i=0;i<c.rows;i++)
     for(int j=0;j<c.cols;j++)
      c.a[i][j] = this.a[i][j].plus(m.a[i][j].times(k));
    return c;
  }

}