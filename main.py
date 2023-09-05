import AverageCreditPeriods as Average

PATH = r'sample input/transaction1.xlsx'
SHEET = 'Sheet1'
PERCHASE_OUTPUT = r'output//Purchase.xlsx'
PAYMENT_OUTPUT = r'output//Payment.xlsx'

data, len = Average.read_excel_file(PATH, SHEET)
data['Amount'] = data['Amount'].fillna(0).astype('int')

transaction = data['Type of transaction']
Payment = data[transaction == 'Payment']
Purchase = data[transaction == 'Purchase']

# sort Date in ascending order
Payment.sort_values(by=['Date'], inplace=True)
Purchase.sort_values(by=['Date'], inplace=True)

Payment = Average.total(Payment)
Purchase = Average.total(Purchase)

Purchase['Total'] = [0 - row['Total'] for index, row in Purchase.iterrows()]

average = Average.compute_average(Payment, Purchase)

print(average)

# Average.write_excel_file(PERCHASE_OUTPUT, 'PERCHASE', Purchase)
# Average.write_excel_file(PAYMENT_OUTPUT, 'PAYMENT', Payment)
