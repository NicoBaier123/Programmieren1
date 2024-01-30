unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, XPMan, Grids, Math;

type aMatrix = array[1..10,1..10] of integer;
type mMatrix = record
  a: aMatrix;
  m,n: integer;
end;

type
  TForm1 = class(TForm)
    StringGrid1: TStringGrid;
    Button1: TButton;
    XPManifest1: TXPManifest;
    ResultGrid: TStringGrid;
    Button2: TButton;
    Button3: TButton;
    Label2: TLabel;
    Label3: TLabel;
    Label1: TLabel;
    Label4: TLabel;
    StringGrid2: TStringGrid;
    procedure Button1Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
    procedure LoadMatrix(var m: mMatrix);
    procedure LoadMatrix2(var m: mMatrix);
    procedure ShowResultMatrix(var m: mMatrix);
  end;

function AlgebrDopoln(var m: mMatrix; i,j: integer): integer;
function Opred(m: mMatrix): integer; // m = n


var
  Form1: TForm1;


implementation

{$R *.dfm}

////////////////////

function MinorIJ(m: mMatrix; i,j: integer): integer;
var
  ii,jj,i1,j1: integer;
  m1: mMatrix;
begin

  m1.m:= m.m-1;
  m1.n:= m.n-1;
  for i1:= 1 to m.m do
   for j1:= 1 to m.n do
   begin
    if (i1>i) then ii:= i1-1
              else ii:= i1;
    if (j1>j) then jj:= j1-1
              else jj:= j1;
    m1.a[ii,jj] := m.a[i1,j1];
   end;

  result:= Opred(m1);
end;

function AlgebrDopoln(var m: mMatrix; i,j: integer): integer;
begin
  result:= round(power(-1,i+j)) * MinorIJ(m,i,j);
end;

function Opred(m: mMatrix): integer; // m = n
var
  i,j: integer;
begin
  if m.m = 1 then
  begin
    result:= m.a[1,1];
    exit;
  end;
  result:= 0;
  for i:= 1 to m.m do
   inc(result, m.a[i,1] * AlgebrDopoln(m,i,1));
end;

procedure AmB(var m1,m2,z: mMatrix); // m1.n = m2.m
var i,j,k: integer;
begin
  z.m := m1.m;
  z.n := m2.n;
  for i:= 1 to m1.m do
   for j:= 1 to m2.n do
   begin
    z.a[i,j]:= 0;
    for k:= 1 to m1.n do
     inc(z.a[i,j],m1.a[i,k]*m2.a[k,j]);
   end;
end;

function Obr(var m1,z: mMatrix): integer; // m1.n = m2.m
var i,j,k: integer;
begin
  z.m := m1.m;
  z.n := m1.n;

  for i:= 1 to m1.m do
   for j:= 1 to m1.n do
     z.a[i,j]:= AlgebrDopoln(m1,j,i);

 result:= Opred(m1);
end;


///////////////////

procedure TForm1.LoadMatrix(var m: mMatrix);
var
  i,j: integer;
begin
  m.n:= -1;
  while StringGrid1.Cells[m.n+1,0] <> '' do
    inc(m.n);
  inc(m.n);

  m.m:= -1;
  while StringGrid1.Cells[0,m.m+1] <> '' do
    inc(m.m);
  inc(m.m);

  for i:= 1 to m.m do
   for j:= 1 to m.n do
    m.a[i,j]:= StrToInt(StringGrid1.Cells[j-1,i-1]);
end;

procedure TForm1.LoadMatrix2(var m: mMatrix);
var
  i,j: integer;
begin
  m.n:= -1;
  while StringGrid2.Cells[m.n+1,0] <> '' do
    inc(m.n);
  inc(m.n);

  m.m:= -1;
  while StringGrid2.Cells[0,m.m+1] <> '' do
    inc(m.m);
  inc(m.m);

  for i:= 1 to m.m do
   for j:= 1 to m.n do
    m.a[i,j]:= StrToInt(StringGrid2.Cells[j-1,i-1]);
end;

procedure TForm1.ShowResultMatrix(var m: mMatrix);
var
  i,j: integer;
begin
 for i:= 0 to ResultGrid.RowCount-1 do
  for j:= 0 to ResultGrid.ColCount-1 do
   ResultGrid.Cells[i,j]:= '';

  for i:= 1 to m.m do
   for j:= 1 to m.n do
    ResultGrid.Cells[j-1,i-1]:= IntToStr(m.a[i,j]);
end;

procedure TForm1.Button1Click(Sender: TObject);
var
  m: mMatrix;
begin
  LoadMatrix(m);
  Label4.Caption:= IntToStr(  Opred(m) );
  ShowResultMatrix(m);
end;

procedure TForm1.Button3Click(Sender: TObject);
var
  z,m,m2: mMatrix;
begin
  LoadMatrix(m);
  LoadMatrix2(m2);
  AmB(m,m2,z);
  ShowResultMatrix(z);
end;

procedure TForm1.Button2Click(Sender: TObject);
var
  z,m: mMatrix;
begin
  LoadMatrix(m);
 Label4.Caption:= IntToStr(  Obr(m,z) );
  ShowResultMatrix(z);
end;

end.
