object Form1: TForm1
  Left = 188
  Top = 236
  Width = 1000
  Height = 372
  Caption = 'Form1'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -14
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 120
  TextHeight = 16
  object Label2: TLabel
    Left = 16
    Top = 48
    Width = 9
    Height = 16
    Caption = 'A'
  end
  object Label3: TLabel
    Left = 320
    Top = 48
    Width = 9
    Height = 16
    Caption = 'B'
  end
  object Label1: TLabel
    Left = 688
    Top = 48
    Width = 38
    Height = 16
    Caption = 'Result'
  end
  object Label4: TLabel
    Left = 624
    Top = 152
    Width = 41
    Height = 16
    Caption = 'Label4'
  end
  object StringGrid1: TStringGrid
    Left = 9
    Top = 79
    Width = 288
    Height = 172
    ColCount = 8
    DefaultColWidth = 32
    DefaultRowHeight = 16
    FixedCols = 0
    RowCount = 8
    FixedRows = 0
    Options = [goFixedVertLine, goFixedHorzLine, goVertLine, goHorzLine, goRangeSelect, goEditing]
    TabOrder = 0
  end
  object Button1: TButton
    Left = 57
    Top = 280
    Width = 99
    Height = 31
    Caption = '|A|'
    TabOrder = 1
    OnClick = Button1Click
  end
  object ResultGrid: TStringGrid
    Left = 689
    Top = 79
    Width = 280
    Height = 173
    ColCount = 8
    DefaultColWidth = 32
    DefaultRowHeight = 16
    FixedCols = 0
    RowCount = 8
    FixedRows = 0
    TabOrder = 2
  end
  object Button2: TButton
    Left = 272
    Top = 280
    Width = 73
    Height = 33
    Caption = 'A^-1'
    TabOrder = 3
    OnClick = Button2Click
  end
  object Button3: TButton
    Left = 168
    Top = 280
    Width = 89
    Height = 33
    Caption = 'A*B'
    TabOrder = 4
    OnClick = Button3Click
  end
  object StringGrid2: TStringGrid
    Left = 329
    Top = 87
    Width = 288
    Height = 172
    ColCount = 8
    DefaultColWidth = 32
    DefaultRowHeight = 16
    FixedCols = 0
    RowCount = 8
    FixedRows = 0
    Options = [goFixedVertLine, goFixedHorzLine, goVertLine, goHorzLine, goRangeSelect, goEditing]
    TabOrder = 5
  end
  object XPManifest1: TXPManifest
    Left = 376
    Top = 16
  end
end
