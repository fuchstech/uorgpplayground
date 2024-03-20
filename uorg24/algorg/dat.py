from datetime import datetime, timedelta

# Başlangıç tarihi
start_date = datetime(2023, 3, 10)

# Gün sayısı
n_days = 356

# Gün ekleme
new_date = start_date + timedelta(days=n_days)

# Haftanın günleri
week_days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

# Yeni tarihin haftanın günü
week_day_name = week_days[new_date.weekday()]

# Çıktı formatı
output = new_date.strftime(f"%d.%m.%Y {week_day_name}")
print(output)
