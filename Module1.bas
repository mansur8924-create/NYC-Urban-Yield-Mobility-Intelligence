Attribute VB_Name = "Module1"
Sub UpdateDashboard()
    Dim ws As Worksheet
    Dim targetHour As String
    Dim filePath As String
    Dim fileNum As Integer
    Dim lineData As String
    Dim dataParts() As String
    Dim found As Boolean
    
    ' --- ARCHITECT'S NOTE: TARGETING ---
    ' WHAT: Setting the sheet and the hour the user typed in C2.
    Set ws = ThisWorkbook.Sheets("Dashboard")
    targetHour = ws.Range("C2").Value
    
    ' Ensure the hour is two digits (e.g., "01" instead of "1") to match SQL format
    If Len(targetHour) = 1 Then targetHour = "0" & targetHour
    
    ' --- ARCHITECT'S NOTE: THE FILE PATH ---
    ' WHAT: Pointing to the CSV 'Bridge' file.
    filePath = "C:\Users\mansu\OneDrive\Desktop\Data Analyst Boot Camp\Data Analyst Projects\The_Metropolis_Mobility Ledger\Hourly_Summary.csv"
    
    fileNum = FreeFile
    Open filePath For Input As #fileNum
    
    ' Skip the header row
    Line Input #fileNum, lineData
    
    found = False
    Do While Not EOF(fileNum)
        Line Input #fileNum, lineData
        dataParts = Split(lineData, ",")
        
        ' dataParts(0) = Hour, (1) = Rides, (2) = Revenue, (3) = Tip
        If dataParts(0) = targetHour Then
            ws.Range("C4").Value = Format(dataParts(2), "$#,##0.00") ' Revenue
            ws.Range("C5").Value = Format(dataParts(3), "$#,##0.00") ' Avg Tip
            ws.Range("C6").Value = dataParts(1)                     ' Rides
            found = True
            Exit Do
        End If
    Loop
    
    Close #fileNum
    
    ' --- ARCHITECT'S NOTE: USER FEEDBACK ---
    If found Then
        MsgBox "Data updated for Hour " & targetHour, vbInformation
    Else
        MsgBox "Hour not found. Please enter 00 through 23.", vbExclamation
    End If
End Sub
