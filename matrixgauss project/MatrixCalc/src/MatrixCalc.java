import javax.microedition.lcdui.*;
import javax.microedition.midlet.*;

public class MatrixCalc extends MIDlet
    implements CommandListener, ItemCommandListener{

    private Display display;
    private Form LogoForm,QForm;
    public MatrixCalc()     {}

    private StringItem str, myRes; 	//Строка
    private ChoiceGroup myChoice;	//Варианты ответов
    private TextField TFMatrixA, TFMatrixB;
   
    //Создаем комманды
    private Command CMD_GO = new Command("Go", Command.ITEM, 1);
    private Command CMD_PRESS = new Command("Press", Command.ITEM, 1); 
    private Command CMD_DOIT = new Command("Do", Command.SCREEN, 1); 
    private Command CMD_EXIT = new Command("Close", Command.EXIT, 1); 
    protected void destroyApp( boolean unconditional ) throws MIDletStateChangeException 
     {
       exitApp(); // вызывает уборщик мусора
      }

    protected void pauseApp()
     {
     }

    protected void startApp() throws MIDletStateChangeException
     {
         if( display == null )
              { 
                  initApp(); 
              }  
     }

    private void initApp()	//Этот метод выполняется при запуске мидлета
     {
         display = Display.getDisplay( this );
         LogoForm=new Form("Matri-tri-ca: Matrix Calculator"); //Создаем первую форму
         LogoForm.setCommandListener(this);
	//Создаем подпись
        str = new StringItem("Matri-tri-ca\n", "http://matri-tri-ca.narod.ru/", Item.HYPERLINK);
	LogoForm.append(str);

        TFMatrixA = new TextField("Matrix A","1 2\n3 4",2048,TextField.ANY);
        TFMatrixB = new TextField("Matrix A","4 2\n4 2",2048,TextField.ANY);
        myChoice = new ChoiceGroup("Select Action",Choice.POPUP);
        myChoice.append("|A|",null);
        myChoice.append("A^-1",null);
        myChoice.append("|B|",null);
        myChoice.append("B^-1",null);
        myChoice.append("A*B",null);
        myChoice.append("A+B",null);
        myChoice.append("A-B",null);
         
        myRes = new StringItem("Result", "\n");
        LogoForm.append(TFMatrixA);
        LogoForm.append(TFMatrixB);
        LogoForm.append(myChoice);
	LogoForm.append(myRes);

	//Добавляем подэкранные кнопки
        LogoForm.addCommand(CMD_DOIT);
        LogoForm.addCommand(CMD_EXIT);
	//Объявляем обработчик команд
        display.setCurrent(LogoForm);
     }
    
    public void exitApp()
     {
         notifyDestroyed(); // уничтожение MIDlet-а
     }
    
    public void commandAction(Command c, Item item) {
    }

    public String doit(String text1, String text2, int n) {
      String mstr = "";
      Matrix m1 = new Matrix(text1);
      Matrix m2 = new Matrix(text2);

      switch(n){
       case 0: mstr = ""+m1.getDeterminant(); break;
       case 1: mstr = ""+m1.getInverse(); break;
       case 2: mstr = ""+m2.getDeterminant(); break;
       case 3: mstr = ""+m2.getInverse(); break;
       case 4: mstr = ""+m1.times(m2); break;
       case 5: mstr = ""+m1.plus(m2,1); break;
       case 6: mstr = ""+m1.plus(m2,-1); break;
      }

      return mstr;
    }


    public void commandAction(Command c, Displayable d) {
        if (c == CMD_DOIT) {
          myRes.setLabel( doit(TFMatrixA.getString(),TFMatrixB.getString(),myChoice.getSelectedIndex()) );
        }
        if (c == CMD_EXIT){exitApp();}	//Команда "Выход"
    } 
    
}
