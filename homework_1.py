from datetime import datetime

n = datetime.now().minute
color = n % 5
if 0 < color < 3:
    print('Горит зелёный!')
else:
    print('DA RED GOEZ FASTA!!!')
