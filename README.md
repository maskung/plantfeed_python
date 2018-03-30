# plantfeed_python 

โปเจคนี้เป็นโปรเจครถน้ำต้นไม้อัตโนมัติและมีการบันทึกข้อมูลขึ้น netpie  

## รายละเอียดระบบ

โปรเจคนี้จะประกอบไปด้วย

* 1.เซนเซอร์วัดความชื้นในดิน
* 2.Raspberry Pi 
* 3.Relay ขับมอเตอร์ 1 channel
 
### การตั้งค่าต่างๆ และสิ่งที่ต้องใข้

ไลบรารีที่ต้องใช้
1.netpie microgear

โค้ดที่ใช้พัฒนา โปรเจคนี้เขียนด้วยภาษาไพธอน พารามิเตอร์ต่างๆ ในการกำหนดให้ระบบทำงานอยู่ทางตอนต้นของโค้ด เป็นดังนี้

```
  
appid = 'xxxx'  #หมายเลข appid ของท่านที่สร้างใน netpie
gearkey = 'xxxx' #key ที่สร้างขึ้น ใน APPID
gearsecret = 'xxxx' #secrate ที่ได้จากการสร้าง key

#--------------------------------------------------------------------------------------

//ขา รีเลย์ และเซนเซอร์ความชื้นกำหนดที่นี่
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)
```
### การติดตั้งและใช้งาน

* 1.ดาวน์โหลดโปรแกรม plantfeed.py ลงที่ไดเรคทอรีที่ท่านต้องการ
* 2.#sudo chmod +x plantfeed.py
* 3../plantfeed.py
การเรียกใช้งานโปรแกรม 

## ผู้เขียน

* **Suphanut Thanyaboon** - *ผู้ริเริ่ม* - [maskung](https://github.com/maskung)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
