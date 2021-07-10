#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add_time(start, duration,stating_date=None):
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    days_l=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    AP=["AM","PM"]

    t_start,ap_start=start.split(" ")


    t_start_h,t_start_m=t_start.split(":")


    duration_h,duration_m=duration.split(":")


    #calculating the Time

    mins=int(t_start_m) + int(duration_m)

    hours=int(t_start_h) + int(duration_h)


    if mins>60:
        mins_final=mins-60
        hours = hours +1
    else:
        mins_final=mins


  
    if hours > 12:

        count=0
        if hours % 12 ==0:
            count=1
            count_h=(hours//12)-1

            for i in range(count_h):
                hours= hours-12
                count = count + 1
        else:
            count_h=hours//12

            for i in range(count_h):
                hours= hours-12
                count = count + 1
        hours_final=hours
    elif hours < 12:
        count=0
        hours_final= hours
    elif hours==12:
        count=1
        hours_final= hours


    #calculating AM or PM

    if ap_start =="AM":
        if (count % 2) == 0:
            ap_final="AM"
        else :
            ap_final="PM"

    if ap_start == "PM":
        if (count % 2) == 0:
            ap_final="PM"
        else :
            ap_final="AM"

#calculating no of days

    if ap_start=="AM" and count!=0:
        daysx=count//2
      
    elif ap_start=="PM" and count!=0:
        daysx=(count+1)//2
      
    else:
        daysx=0
    if daysx==1:
        day_final="(next day)"
    elif daysx>1:
        day_final= f"({daysx} days later)"
    elif daysx==0:
        day_final=""
  


  #calculating the day
    if stating_date==None:
        date=""
    else:
        stating_date_i_l=stating_date.lower()
        index=days_l.index(stating_date_i_l)
        index_now=index + int(daysx)
        index_now_t=index_now + 1
        if index_now_t  > len(days):
            while index_now  >= len(days):
                index_now = index_now -7
            date=f", {days[index_now]}"
        else:
            date=f", {days[index_now]}"


    new_time=f"{hours_final}:{mins_final:02d} {ap_final}{date} {day_final}"
#     new_time=str(hours_final) + ":" + str(mins_final) + " " + ap_final
    new_time=new_time.rstrip()

    return new_time







# In[9]:


"""
add_time("3:00 PM", "3:10")
 Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
 Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
 Returns: 12:03 PM

add_time("10:10 PM", "3:30")
 Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
 Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
 Returns: 7:42 AM (9 days later)
"""
add_time("6:30 PM", "205:12")

