class Fraction {
  int n, d;
 
  int gcd(int a, int b) {
    a = Math.abs(a);
    b = Math.abs(b);
    if ( !(a>0 && b>0) ) return a+b;    // b=0 is error value ?
    int t;
    while ( b>0 ) {
      t = a % b;
      a = b;
      b = t;
    }
    return a;
  }
  Fraction() {
    this.n = 0;
    this.d = 1;
  }
  Fraction(int n) {
    this.n = n;
    this.d = 1;
  }
  Fraction(int n,int d) {
    if(d==0) {
      this.d = 1;//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      this.n = 999999999;
     // return null; //Error!
    }
  
    if(n==0)
      d=1;
    if(d<0) {
      n = -n;
      d = -d;
    }
    int g = gcd(n,d);
    this.n = n/g;
    this.d = d/g;
  }
  Fraction(Fraction f) {
    this.n = f.n;
    this.d = f.d;
  }
  Fraction(String s) {// "321/12"
    int i = s.indexOf('/');
    int nn, dd; 
    if(i!=-1){
      nn = Integer.parseInt(s.substring(0,i));
      dd = Integer.parseInt(s.substring(i+1));
    }else{
      nn = Integer.parseInt(s);
      dd = 1;
    }
    n= nn;
    d= dd;
    if(d==0) {
      this.d = 1;//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      this.n = 999999999;
     // return null; //Error!
    }
  
    if(n==0)
      d=1;
    if(d<0) {
      n = -n;
      d = -d;
    }
    int g = gcd(n,d);
    this.n = n/g;
    this.d = d/g;
    
  }
  public String toString() {
    return ""+this.n + (this.d!=1?"/"+this.d:"");
  }
  int cmp(Fraction f) {
    return (this.n*f.d - this.d*f.n);
  }
  int cmp(int n) {
    return (this.n - this.d*n);
  }

  Fraction times(int n) {
    return new Fraction( this.n*n, this.d );
  }
  Fraction times(Fraction f) {
    return new Fraction( this.n*f.n, this.d*f.d );
  }

  Fraction divide(int n) {
    return new Fraction( this.n, this.d*n );
  }
  Fraction divide(Fraction f) {
    return new Fraction( this.n*f.d, this.d*f.n );
  }

  Fraction plus(int n) {
    return new Fraction( this.n+n*this.d, this.d );
  }
  Fraction plus(Fraction f) {
    return new Fraction( this.n*f.d + this.d*f.n, this.d*f.d );
  }

  Fraction minus(int n) {
    return new Fraction( this.n-n*this.d, this.d );
  }
  Fraction minus(Fraction f) {
    return new Fraction( this.n*f.d - this.d*f.n, this.d*f.d );
  }
  Fraction minus() {
    return new Fraction( -this.n, this.d);
  }
  
  Fraction abs() {
    return new Fraction( (this.n>0?this.n:-this.n) , this.d );
  }
  Fraction getcopy() {
    return new Fraction(this);
  }
}

// tests
//    f=new Fraction(1,-2); 
//    alert(f); 
//    g=new Fraction(1,3); 
//    alert(g.plus(f));
