# LumiTouch: Lighting Adaptation Through Interactive Sensing

`This is a final project for CS437 (Internet of Things) Spring 2024 at UIUC`  

LumiTouch is a project for adaptive lighting system with interactive sensors including force sensor resistor (FSR) and ultrasonic sensor. Our system is based on Raspberry Pi 4 Model B to process the pressure and distance signals and control the LEDs. 

[Video](https://drive.google.com/file/d/1xwM0cCyaitssnh8i8X5o6ZnUSOekoxKG/view) [Report](/assets/CS437_final.pdf)

![Result](/assets/results.png)

## Hardware

To reproduce our system, we include our hardware list here.

- [Raspberry Pi 4 Model B](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/?th=1)
- [Force Sensor Resistor](https://www.amazon.com/gp/product/B00B887DBC/ref=ox_sc_rp_title_rp_1?smid=&psc=1&pf_rd_p=a31e89a8-26da-4517-9344-bed7a347818e&pd_rd_wg=lWrQs&pd_rd_i=B00B887DBC&pd_rd_w=4JFQh&content-id=amzn1.sym.a31e89a8-26da-4517-9344-bed7a347818e&pd_rd_r=M8YXHJD3M17RTNNPGG53)
- [Ultrasonic Sensor](https://www.amazon.com/Ultrasonic-Distance-Transmitter-Receiver-MEGA2560/dp/B07PFCVM9D/ref=sr_1_2_sspa?crid=1NZS60W6M6R9B&dib=eyJ2IjoiMSJ9.E2SIkElJhtFWCJCHL5Q6Y3vyMcZDuOOj1lHVUVIASi8LzqXYBZM-F-m0eAwK81wRRgms80CS4qPrBF7Rcu3Wa-5trjq5y7geeSSaH4WkjwtGTP6RwCU5uOJudILfInA_v-lSPZxCSuRHeEDtMnf--HqA9lpakDKEJGKkyURMN66gOchTH3_7XC3aygGJdPhBcsuRWGHFp2BDhXTaan9ett2tPOnpJ4-q2TRRsksTvHM.FkAg6R0gnlDbgTkGmq56ViKqcdwyfoDXgLhLk3SzpzQ&dib_tag=se&keywords=ultrasonic+sensor&qid=1714969087&sprefix=ultrasonic+sensor%2Caps%2C81&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
- [LEDs](https://www.amazon.com/dp/B07PG84V17?ref=ppx_yo2ov_dt_b_product_details&th=1)
- [Jumper wire](https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78/ref=sr_1_3_sspa?crid=S9DNVB4ABY8P&dib=eyJ2IjoiMSJ9.q-Pd8h6QV_QsVCQvh3sPUCmjtfxnhG7-b0_O6MwzKaqTnL8KhOW6LJ-3w7F0XBQNJINSHxVsUG5B5KNmFW-U-zRKK6B4NT5aijS7Mq5P5mFpCWui0zgYoUOX2jKaXKcJs1pggnIGQoLXMvJ2s69qQaIhahTZqN-DffmtnFwycPU1PJ4aLO1v9DCVKAmfeEuHNQcg6jC07goV5hau8nOH9A65da7S46PgWwOgMBqPVMcAddLxmxGaWsKusEQU-S8JnDfN60ZIZ3y70YRBhViLREop2yvNZB8JG_7QFkprxtk.AnPQPPakRwT-bemjlR1slT4rN-veDXzFayih25KMqWs&dib_tag=se&keywords=jumper+wire&qid=1714969177&s=hi&sprefix=jumper+wire%2Ctools%2C77&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1).
- [Breadboard](https://www.amazon.com/EL-CP-003-Breadboard-Solderless-Distribution-Connecting/dp/B01EV6LJ7G/ref=sr_1_2_sspa?dib=eyJ2IjoiMSJ9.0XjhQpvsxVGvVwki4XDjTQ1NwlQgUbmPkISrVDMlHvUJ74nv754rZAUCzJ7kgtUDf69eG2ZWZWGIyB7vcX6DrfRQsvRE5Y6nBYHKO0GjEzly97yXZFH1kIuG22RXmAgdDWdyWmF4j-Ls-nibY0WK23wWJ3ejG4UTci44b910zCBA8g0qw7atUayr4oDgGI0T0NJF5D-hoS-DGQ7PwztIJReIth1MW1P8tnEzI7DmZmY.rzbqyWbg1d5iXKyCH5f8G97qX3Oz65M3FymNBd56tmY&dib_tag=se&keywords=breadboard&qid=1714969210&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)

## Usage

### Pressure detection
```shell
Python src/fsr_raspberry.py
```

### Single Light with Interactive Sensing
```shell
Python src/ultrasonic.py
```

### Multi Lights with Interactive Sensing
```shell
Python src/ultrasonic_multi.py
```

## Acknowledgement
- [How to use Force Sensitive Resistors with a Raspberry Pi and a ADS1015 ADC](https://www.youtube.com/watch?v=SX0636jmktM)
