from django.shortcuts import render

from django.shortcuts import render
import openpyxl


# Create your views here.


def index(request):
    if "GET" == request.method:
        return render(request, 'excel.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        new = request.POST["nctc"]
        nwsal = int(new)

        wb = openpyxl.load_workbook(excel_file)

        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()

        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))

            excel_data.append(row_data)

        for i in excel_data:
            global a
            if i[0] == ('ctc'):
                a = int(i[1])
        dict = {'Basic Salary': [], 'HRA': [], 'Special Allowance': [], 'Employer PF': [], 'Employer ESI': [],
                'Base Salary': [], 'Annual Short-Term Bonus': [], 'Other Allowance (Internet)': [], 'total amound': []}
        row = list()

        for i in excel_data:
            global bs, p1

            if i[0] == ('Basic Salary'):
                a1 = int(i[1])
                p1 = (a1 * 100) / a
                bs = (a * p1) / 100
                dict['Basic Salary'].append(bs)
        for i in excel_data:
            global hra, p2
            if i[0] == ('HRA'):
                a2 = int(i[1])
                p2 = (a2 * 100) / a
                hra = (a * p2) / 100
                dict['HRA'].append(hra)
        for i in excel_data:
            global sa, p3
            if i[0] == ('Special Allowance'):
                a3 = int(i[1])
                p3 = (a3 * 100) / a
                sa = (a * p3) / 100
                dict['Special Allowance'].append(sa)
        for i in excel_data:
            global pf, p4
            if i[0] == ('Employer PF'):
                a4 = int(i[1])
                p4 = (a4 * 100) / a
                pf = (a * p4) / 100
                dict['Employer PF'].append(pf)
        for i in excel_data:
            global esi, p5
            if i[0] == ('Employer ESI'):
                a5 = int(i[1])
                p5 = (a5 * 100) / a
                esi = (a * p5) / 100
                dict['Employer ESI'].append(esi)
        # global total
        total = bs + esi + pf + sa + hra
        dict['Base Salary'].append(total)

        for i in excel_data:
            global p7, astb
            if i[0] == ('Annual Short-Term Bonus'):
                a7 = int(i[1])
                p7 = (a7 * 100) / a
                astb = (a * p7) / 100
                dict['Annual Short-Term Bonus'].append(astb)
        for i in excel_data:
            global p8, oa
            if i[0] == ('Other Allowance (Internet)'):
                a8 = int(i[1])
                p8 = (a8 * 100) / a
                oa = (a * p8) / 100
                dict['Other Allowance (Internet)'].append(oa)

        tot = total + astb + oa
        dict['total amound'].append(tot)

        row.append(dict)
        mlist = row

        newdict = {'newbasicsalary':[], 'newHRA': [], 'new Special Allowance': [], 'new Employer PF': [],
                   'new Employer ESI': [],
                   'new Base Salary': [], 'new Annual Short-Term Bonus': [], 'new Other Allowance (Internet)': [],
                   'total amo': []}
        row2 = list()
        b = (nwsal * p1) /100
        b1 = (nwsal * p2) / 100
        b2 = (nwsal * p3) /100
        b3 = (nwsal * p4) / 100
        b4 = (nwsal * p5) / 100
        total2 = b + b1 + b2 + b3 + b4
        newdict['new Base Salary'].append(total2)
        b5 = (nwsal * p7)/ 100
        b6 = (nwsal * p8) / 100

        totalamound = total2 + b5 + b6

        newdict['newbasicsalary'].append(b)
        newdict['newHRA'].append(b1)
        newdict['new Special Allowance'].append(b2)
        newdict['new Employer PF'].append(b3)
        newdict['new Employer ESI'].append(b4)
        newdict['new Annual Short-Term Bonus'].append(b5)
        newdict['new Other Allowance (Internet)'].append(b6)
        newdict['total amo'].append(totalamound)

        row2.append(newdict)
        newlist = row2

        return render(request, 'excel.html', {"mlist": mlist, "newlist": newlist})
