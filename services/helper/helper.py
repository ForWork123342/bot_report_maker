from services.google_sheets import get_sheet_data



def change_table(data):
    name_list = get_sheet_data("workers")
    report_data = data
    for i in range(len(name_list)):
        if report_data[0][1] == name_list[i][0]:
            for j in range(len(report_data)):
                report_data[j][1] = (name_list[i][1] + ' ' + name_list[i][2] + ' ' + name_list[i][3])

    products = get_sheet_data("products")
    for i in range(len(report_data)):
        for j in range(len(products)):
            if report_data[i][2] == products[j][0]:
                report_data[i][2] = products[j][1]

    packaging = get_sheet_data("packaging")
    for i in range(len(report_data)):
        for j in range(len(packaging)):
            if report_data[i][3] == packaging[j][0]:
                report_data[i][3] = packaging[j][1]

    for row in report_data:
        print(row)
    
    return report_data