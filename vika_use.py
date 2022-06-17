from scipy.fft import dst
from vika import Vika

vika = Vika("usk5wrsZJhDn269TgtUg9pw")
dst = vika.datasheet("dstVj9XtNASyHgoYDl")
space_id = "spcZZu4MXAl6N"

records = dst.records.all(viewId="viwHBkkBKgFCY")
for record in records:
  print(record.json())  