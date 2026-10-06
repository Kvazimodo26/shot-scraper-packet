# shot-scraper-packet
rpm packet for shot-scraper

Для установки пакета требуется зависимость:
python3-module-playwright

Этого пакета в репозитории alt я не нашел, поэтому установил через pip:
pip3 install 'playwright>=1.62.0'

И после установки остальных зависимостей установил пакет без зависимостей:
rpm --nodeps -Uvh python3-module-shot-scraper-1.12-alt1.noarch.rpm

# Сначала лучше запускать установку без флага --nodeps, чтобы установить недостающие пакеты.
