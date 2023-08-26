try:
    try:
        import ephem
        import math
        import webbrowser
        import time as t
        import datetime
        import pandas as pd
    except Exception as e:
        print("Please install the necessary modules")
        print(''' ephem
         math
         webbrowser
         time
         datetime
         pandas''')
    def redirection():#working properly (test 4 conductedd)
        webbrowser.open("https://www.findmylatlng.com/")
        t.sleep(10)
    def guided():
        print("Guidation Coordinization Initialized")
        t.sleep(1)
        print("Step 0: Allowe permission to acceess location in the website")
        t.sleep(1)
        print("Step 1: Wait for few seconds")
        t.sleep(2)
        print("Step 2: Your coordinates will be shown in the white box")
        t.sleep(2)
        print("Step 3: Copy the coordinates  and paste it ")
        t.sleep(3)
        print("Step 4: There will be a 20 second window for you to get your coordinates")
        t.sleep(1)
        print("Step 5: Example coordinates - 21.00321,321.43932")
        t.sleep(8)
        print("Redirecting you towards")
        t.sleep(1)
        redirection() 
    def introduction():
        text = '''                          Project by Jammed-Jermy 
                             .                                      .    '             .      .  "   '
         ..             '                       .  .  .                 '      '.
         .            .              . "`       .   ..         .                            .
                     .                             .                         '     '.
                                .    '       _______________                .                 .     .
                                         ==c(___(o(______(_()                       ..
                                                    \=\                                  .             . .
                                                     )=\                                     .
                                                   //||\\                          ..
                                                  // || \\                                .
                                                 //  ||  \\  
                                                //   ||   \\
                                               //          \\
                                PROJECT ON Celesital Object Tracking'''

        for x in text:
            print(x, end='', flush=True)
            if x == ' ':
                t.sleep(0.0001)  
            else:
                t.sleep(0.08)  
        print()
    def menu():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\t    ---------Celestial Object Tracker------------")
        print("\t\t----------------------------------")
        print("\t\t| 0. Find Cordinates             |")
        print("\t\t|--------------------------------|")
        print("\t\t| 1. Check Position              |")
        print("\t\t| 2. Track Position              |")
        print("\t\t| 3. Sunset Time                 |")
        print("\t\t| 4. Sunrise Time                |")
        print("\t\t| 5. All Planets Visibility      |")
        print("\t\t| 6. Check Twilights             |")
        print("\t\t| 7. Exit                        |")
        print("\t\t----------------------------------")
    def menu2():
        t.sleep(5)
        print("\t    ---------Celestial Object Tracker------------")
        print("\t\t----------------------------------")
        print("\t\t| 1. Check Position              |")
        print("\t\t| 2. Track Position              |")
        print("\t\t| 3. Sunset Time                 |")
        print("\t\t| 4. Sunrise Time                |")
        print("\t\t| 5. All Planets Visibility      |")
        print("\t\t| 6. Check Twilights             |")
        print("\t\t| 7. Exit                        |")
        print("\t\t----------------------------------")
    def sunrise():
        print("Initialized")
        city=ephem.Observer()
        city.lon ='your_longitude'
        city.lat ='your_latitude'
        city.date = ephem.now()
        sun=ephem.Sun()
        sunrise=ephem.localtime(city.next_rising(sun))
        print(sunrise.strftime("%H'o clock at %M Minutes"))
    def chart():
        print("Calculating.")
        t.sleep(1)
        print("Calculating..")
        t.sleep(1)
        print("Calculating...")
        t.sleep(1)
        city=ephem.Observer()
        city.lon ='your_longitude'
        city.lat ='your_latitude'
        city.date =ephem.now()
        mercury = ephem.Mercury(city)
        mercury_az = round(math.degrees(mercury.az), 2)
        mercury_alt = round(math.degrees(mercury.alt), 2)
        mercury_phase = round(mercury.phase, 2)
        mercury_visibility = ""

        if mercury_phase < 50 or mercury_alt <18:
            mercury_visibility = "Not Visible"
        elif mercury_phase >= 50 and mercury_phase < 70 and mercury_alt >18:
            mercury_visibility = "Semi-Visible"
        elif mercury_alt>18 and mercury_phase>70:
            mercury_visibility = "Visible"
        else:
            print(mercury_alt,mercury_phase)

        venus = ephem.Venus(city)
        venus_az = round(math.degrees(venus.az), 2)
        venus_alt = round(math.degrees(venus.alt), 2)
        venus_phase = round(venus.phase, 2)
        venus_visibility = ""

        if venus_phase < 50 or venus_alt <18:
            venus_visibility = "Not Visible"
        elif venus_phase >= 50 and venus_phase < 70 and venus_alt >18:
            venus_visibility = "Semi-Visible"
        elif venus_alt>18 and venus_phase>70:
            venus_visibility = "Visible"
        else:
            print(venus_alt,uranus_phase)

        mars = ephem.Mars(city)
        mars_az = round(math.degrees(mars.az), 2)
        mars_alt = round(math.degrees(mars.alt), 2)
        mars_phase = round(mars.phase, 2)
        mars_visibility = ""

        if mars_phase < 50 or mars_alt <18:
            mars_visibility = "Not Visible"
        elif mars_phase >= 50 and mars_phase < 70 and mars_alt >18:
            mars_visibility = "Semi-Visible"
        elif mars_alt>18 and mars_phase>70:
            mars_visibility = "Visible"
        else:
            print(mars_alt,mars_phase)

        jupiter = ephem.Jupiter(city)
        jupiter_az = round(math.degrees(jupiter.az), 2)
        jupiter_alt = round(math.degrees(jupiter.alt), 2)
        jupiter_phase = round(jupiter.phase, 2)
        jupiter_visibility = ""

        if jupiter_phase < 50 or jupiter_alt <18:
            jupiter_visibility = "Not Visible"
        elif jupiter_phase >= 50 and jupiter_phase < 70 and jupiter_alt >18:
            jupiter_visibility = "Semi-Visible"
        elif jupiter_alt>18 and jupiter_phase>70:
            jupiter_visibility = "Visible"
        else:
            print(jupiter_alt,jupiter_phase)

        saturn = ephem.Saturn(city)
        saturn_az = round(math.degrees(saturn.az), 2)
        saturn_alt = round(math.degrees(saturn.alt), 2)
        saturn_phase = round(saturn.phase, 2)
        saturn_visibility = ""
#https://pastebin.com/fkS7xB0H
        if saturn_phase < 50 or saturn_alt <18:
            saturn_visibility = "Not Visible"
        elif saturn_phase >= 50 and saturn_phase < 70 and saturn_alt >18:
            saturn_visibility = "Semi-Visible"
        elif saturn_alt>18 and saturn_phase>70:
            saturn_visibility = "Visible"
        else:
            print(saturn_alt,saturn_phase)

        uranus = ephem.Uranus(city)
        uranus_az = round(math.degrees(uranus.az), 2)
        uranus_alt = round(math.degrees(uranus.alt), 2)
        uranus_phase = round(uranus.phase, 2)
        uranus_visibility = ""

        if uranus_phase < 50 or uranus_alt <18:
            uranus_visibility = "Not Visible"
        elif uranus_phase >= 50 and uranus_phase < 70 and uranus_alt >18:
            uranus_visibility = "Semi-Visible"
        elif uranus_alt>18 and uranus_phase>70:
            uranus_visibility = "Visible"
        else:
            print(uranus_alt,uranus_phase)

        neptune = ephem.Neptune(city)
        neptune_az = round(math.degrees(neptune.az), 2)
        neptune_alt = round(math.degrees(neptune.alt), 2)
        neptune_phase = round(neptune.phase, 2)
        neptune_visibility = ""

        if neptune_phase < 50 or neptune_alt <18:
            neptune_visibility = "Not Visible"
        elif neptune_phase >= 50 and neptune_phase < 70 and neptune_alt >18:
            neptune_visibility = "Semi-Visible"
        elif neptune_alt>18 and neptune_phase>70:
            neptune_visibility = "Visible"
        else:
            print(neptune_alt,neptune_phase)
        sun = ephem.Sun(city)
        sun_az = round(math.degrees(sun.az), 2)
        sun_alt = round(math.degrees(sun.alt), 2)
        sun_phase = round(sun.phase, 2)
        sun_visibility = ""

        if sun_phase < 50 or sun_alt < 0:
            sun_visibility = "Not Visible"
        elif sun_phase >= 50 and sun_phase < 70 and sun_alt > 10:
            sun_visibility = "Semi-Visible"
        elif sun_alt>18 and sun_phase>70:
            sun_visibility = "Visible"
        else:
            sun_visibility = "Not Visible"

        moon = ephem.Moon(city)
        moon_az = round(math.degrees(moon.az), 2)
        moon_alt = round(math.degrees(moon.alt), 2)
        moon_phase = round(moon.phase, 2)
        moon_visibility = ""

        if moon_phase < 50 or moon_alt < 0:
            moon_visibility = "Not Visible"
        elif moon_phase >= 50 and moon_phase < 70 and moon_alt > 10:
            moon_visibility = "Semi-Visible"
        elif moon_alt>18 and moon_phase>70:
            moon_visibility = "Visible"
        else:
            print(moon_alt,moon_phase)

        data = {
            'Planet': ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune','Sun','Moon'],
            'Azimuth': [mercury_az, venus_az, mars_az, jupiter_az, saturn_az, uranus_az, neptune_az,sun_az,moon_az],
            'Altitude': [mercury_alt, venus_alt, mars_alt, jupiter_alt, saturn_alt, uranus_alt, neptune_alt,sun_alt,moon_alt],
            'Phase': [mercury_phase, venus_phase, mars_phase, jupiter_phase, saturn_phase, uranus_phase, neptune_phase,sun_phase,moon_phase],
            'Visibility': [mercury_visibility, venus_visibility, mars_visibility, jupiter_visibility, saturn_visibility,
                        uranus_visibility, neptune_visibility,sun_visibility,moon_visibility]
            }

        df = pd.DataFrame(data)
        print(df)
    def sunset():
        user=int(input("1.Calculated or 2.PreDefine?"))
        if user==1:
            print("This will take 1 Minute")
            t.sleep(1)
            print("Runing")
            city=ephem.Observer()
            city.lon ='your_longitude'
            city.lat ='your_latitude'
            city.date = ephem.now()
            sun=ephem.Sun()
            sun.compute(city)
            altitude1=math.degrees(sun.alt)
            if altitude1<0:
                print("The Sun has already Set")
                exit()
            t.sleep(60)
            city.date = ephem.now()
            sun.compute(city)
            altitude2=math.degrees(sun.alt)
            city.date = ephem.now()
            sun.compute(city)
            Distance=math.degrees(sun.alt)
            speed=altitude1-altitude2
            sunset_time=Distance/speed
            sunset_time_hours=round(sunset_time/60,2)
            hours=int(sunset_time_hours)
            minutes=round((sunset_time_hours-hours)*60)
            print(f"Time left until sunset {hours}:{minutes}")
            x=datetime.datetime.now()
            time=x.time()
            hour = int(time.strftime('%H'))
            minute=int(time.strftime('%M'))
            new_min=minute+minutes
            new_hour=hour+hours
            if new_hour >12:
                new_hour =new_hour-12
                if new_min>60:
                    new_min=new_min-60
                    print("Sunset time:",new_hour,minutes+minute)
                else:
                    print("Sunset time:",new_hour,new_min)
            else:
                if new_min>60:
                    new_min=new_min-60
                    print("Sunset time:",new_hour,new_min)
                else:
                    print("Sunset time:",new_hour,new_min)
        else:
            city=ephem.Observer()
            city.lon ='your_longitude'
            city.lat ='your_latitude'
            city.date = ephem.now()
            sun=ephem.Sun()
            sunset=ephem.localtime(city.next_setting(sun))
            print(sunset.strftime("%H'o clock at %M Minutes"))
        
    def calculate_twilight():
        city = ephem.Observer()
        city.lon ='your_longitude'
        city.lat ='your_latitude'
        city.date = ephem.now()
        city.horizon="-18"
        sun=ephem.Sun()
        sun.compute(city)
        astro=ephem.localtime(city.next_setting(sun))
        astro=(astro.strftime("%H'o clock at %M Minutes"))
        city.horizon="-12"
        nautical=ephem.localtime(city.next_setting(sun))
        nautical=(nautical.strftime("%H'o clock at %M Minutes"))
        city.horizon="-6"
        civil=ephem.localtime(city.next_setting(sun))
        civil=(civil.strftime("%H'o clock at %M Minutes"))
        print(f'''Civil Twilight at {civil}
    Nautical Twilight at {nautical}
    Astronomical Twilight at {astro} ''')
    xz=0
    sam=0
    if sam==0:  
        introduction()   # COMMENTIZE ME TO SKIP INTRODUCTION
        sam+=1          
        t.sleep(2)
        print("# COMMENTIZE Introduction() in the code to SKIP introduction everytime")
        t.sleep(4)
    menu()
    while True:
        if xz==0:
            xz=1
        else:
            menu2()
        x=input("RESPONSE: ")
        if x=="1":

            observer = ephem.Observer()
            observer.lon ='your_longitude'
            observer.lat ='your_latitude'

            observer.date =ephem.now()

            x=input("Enter a Celestial Body name:")
            if x.title() == "Moon":
                body=ephem.Moon()
            elif x.title() == "Sun":
                body=ephem.Sun()
            elif x.title() == "Mercury":
                body=ephem.Mercury()
            elif x.title() == "Venus":
                body=ephem.Venus()
            elif x.title() == "Mars":
                body=ephem.Mars()
            elif x.title() == "Jupiter":   
                body=ephem.Jupiter()
            elif x.title() == "Saturn":
                body=ephem.Saturn()
            elif x.title() == "Uranus":
                body=ephem.Uranus()
            elif x.title() == "Neptune":
                body=ephem.Neptune()
            elif x.title() == "Pluto":
                body=ephem.Pluto()
            else:
                print("please enter a valid obbject")
                exit()
            #Calculation
            body.compute(observer)
            azimuth = math.degrees(body.az)
            altitude = math.degrees(body.alt)
            altitude=round(altitude)
            azimuth=round(azimuth)
            #clock_system
            azimuth=azimuth/30
            hours=int(azimuth)
            minutes=round((azimuth-hours)*60)
            print("Calculating.")
            t.sleep(1)
            print("Calculating..")
            t.sleep(1)
            print("Calculating...")
            t.sleep(1)
            print("Look at",hours,"o'clock and",minutes,"minutes",end=' ')
            print("At",altitude,"Degrees")
        elif x=="2":
            try:
                y=int(input("For how much time do you want to track the position? (In minutes):"))
                interval=float(input("Enter the interval inbetween the tracking reports(seconds):"))
            except ValueError:
                print("Please enter a valid number")
                exit()
            observer = ephem.Observer()

            observer.lon ='your_longitude'
            observer.lat ='your_latitude'

            observer.date =ephem.now()
            #TAKING THE INTERESTED CELESTIAL OBJECTS

            x=input("Enter a Celestial Body name: ")
            if x.title() == "Moon":
                body=ephem.Moon()
            elif x.title() == "Sun":
                body=ephem.Sun()
            elif x.title() == "Mercury":
                body=ephem.Mercury()
            elif x.title() == "Venus":
                body=ephem.Venus()
            elif x.title() == "Mars":
                body=ephem.Mars()
            elif x.title() == "Jupiter":   
                body=ephem.Jupiter()
            elif x.title() == "Saturn":
                body=ephem.Saturn()
            elif x.title() == "Uranus":
                body=ephem.Uranus()
            elif x.title() == "Neptune":
                body=ephem.Neptune()
            elif x.title() == "Pluto":
                body=ephem.Pluto()
            else:
                print("please enter a valid obbject")
                exit()
            #Calculation
            y=y*60
            y=int(y/interval)
            body.compute(observer)
            azimuth =math.degrees(body.az)
            altitude = round(math.degrees(body.alt),3)
            #altitude=round(altitude)
            #azimuth=round(azimuth)
            #clock_system
            azimuth=azimuth/30
            hours=int(azimuth)
            minutes=round((azimuth-hours)*60)
            t.sleep(1)
            print("\t\t|Directions|Altitude|")
            print(f"\t\t|   {hours}:{minutes}   | {altitude} |")
            starting_time=datetime.datetime.now()
            starting_time=starting_time.strftime("%H:%M:%S")
            for i in range(y):
                t.sleep(interval)
                observer.date = ephem.now()
                body.compute(observer)
                azimuth2 = math.degrees(body.az)
                altitude2 = round(math.degrees(body.alt),3)
                #altitude2=round(altitude2)
                #azimuth2=round(azimuth2)
                #clock_system
                azimuth2=azimuth2/30
                hours2=int(azimuth2)
                minutes2=round((azimuth2-hours2)*60)
                if azimuth2==azimuth:
                    #az2 changes #minutes 2 changes
                    continue
                else:
                    print(f"\t\t|   {hours2}:{minutes2}   | {altitude2} |")
                    azimuth=azimuth2
                    altitude=altitude2
                    hours=hours2
                    minutes=minutes2
            ending_time=datetime.datetime.now()
            ending_time=ending_time.strftime("%H:%M:%S")
            print(f'''Starting time= {starting_time}
                ending_time={ending_time}"
                Total Time Tracked={ending_time-starting_time}''')  
            print("Exited")
        elif x=="3":
            sunset()
        elif x=="4":
            sunrise()
        elif x=="5":
            chart()
        elif x=="7":
            print("Exited")
            exit()
        elif x=="6":
            calculate_twilight()
        elif x=='0':
            guided()
        else:
            print("Value Eror")
except Exception as e:
    print("Please replace 'your_longitude' with your actual longitudes and 'your_latitude' with your actual latitude")
