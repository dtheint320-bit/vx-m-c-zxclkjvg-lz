import streamlit as p
import pandas as m
import altair as q
import folium
from streamlit_folium import st_folium

aw = p.sidebar.selectbox(label= "Menu", options= ["Home", 
                                                  "Departments",
                                                   "Doctor List And Salary Analysis"
                                                     , "Our Location"])

if aw == "Home":
    nb = "🏥 Welcome to Lin Kha Hospital"

    qw = "Your Health, Our Priority"

    am = '''  -Welcome to Lin Kha Hospital, where we are committed to providing friendly, reliable, and quality healthcare for everyone. Our team of caring doctors and medical professionals is here to support you and your family.

About Us

-Lin Kha Hospital provides a comfortable environment with professional healthcare services. We focus on making every patient's experience safe, simple, and welcoming.'''

    b = '''-We believe that healthcare is not only about treating illness, but also about listening to patients, understanding their needs, and helping them feel comfortable throughout their healthcare journey.

-At Lin Kha Hospital, our team consists of dedicated doctors, nurses, healthcare professionals, and support staff who work together to provide a positive experience for every patient. We aim to maintain a friendly and respectful environment where patients and their families can feel comfortable asking questions, discussing their concerns, and receiving professional guidance.

-Our hospital provides a range of general healthcare services designed to support the everyday health needs of individuals and families. From routine checkups and consultations to basic medical care and health guidance, our team is ready to assist patients with care and attention. We focus on providing services in an organized and convenient way so that patients can spend less time worrying about the process and more time focusing on their health.

-We understand that visiting a hospital can sometimes feel stressful or uncomfortable. That is why we try to create an environment that feels welcoming from the moment a patient arrives. Our staff are committed to treating every person with kindness, patience, and respect, regardless of their background or circumstances. We believe that a good healthcare experience begins with good communication and genuine care.

-Patient safety and comfort are important parts of our approach. We aim to maintain a clean, organized, and professional environment while following appropriate healthcare practices. Our team works carefully to ensure that patients receive clear information and appropriate support during their visit.

-Lin Kha Hospital also believes that prevention and healthy living are important parts of healthcare. Regular health checkups, healthy habits, and early attention to health concerns can help people maintain their well-being. Through our healthcare services and friendly guidance, we hope to encourage individuals and families to take an active role in looking after their health.

-Our vision is to become a hospital that people can feel comfortable trusting when they need healthcare support. We continuously aim to improve our services, create a better patient experience, and maintain a high standard of professionalism. Every patient is important to us, and every visit is an opportunity for our team to provide better care.

-Whether you are visiting for a routine checkup, seeking medical advice, supporting a family member, or simply looking for a reliable healthcare provider, Lin Kha Hospital is here to welcome you. Our team is ready to listen, assist, and provide the support you need in a friendly and professional environment.

-At Lin Kha Hospital, we believe that healthcare should be built on care, trust, respect, and compassion. Your well-being is at the heart of everything we do, and we are proud to serve our community by making quality healthcare feel more approachable and comfortable.'''

    p.title(nb)
    p.header(qw)
    p.markdown(am)
    p.markdown(b)

    ti = {"Monday": "6:00AM to 7:00PM", 
           "Tuesday": "6:00AM to 7:00PM",
           "Wednesday": "7:00AM to 7:50PM",
           "Thursday": "7:00AM to 7:50PM",
           "Friday": "8:00AM to 9:00PM"}

    p.subheader("More Informations About Us⬇️")

    with p.expander(label= "Opening Hour"):
        a = m.DataFrame(list(ti.items()), columns= ["Day", "Time"])
        p.table(a)

    with p.expander("Contact Us"):
        p.code("Phone: +09899086006")
        p.code("Email: Drmyosat90@gmail.com")
        p.code("Location: Near သစ်ထူးောင် စတိုး," 
        " 270 Strand Rd," 
        " Yangon")

if aw == "Departments":
    p.header("Comprehensive Healthcare Under One Roof")
    
    p.write("-From emergency care and general medicine " 
    "to specialized treatments, " 
    "our departments are dedicated " 
    "to providing safe, effective, "
    "and compassionate healthcare for every patient.")

    p.header("🏥 Our Departments")
    p.subheader("1. Emergency Department")
    p.image("emer.jpg")
    p.write("""Provides immediat"e medical care for serious
      injuries, accidents, sudden illnesses, 
      and other life-threatening conditions.""")
    p.subheader("Services")
    p.write("-urgent medical evaluation")
    p.write("-trauma treatment")
    p.write("-24/7 emergency")

    p.subheader("2.Cardiology Department")
    p.image("cardi.jfif")
    p.write("Specializes in diagnosing and treating diseases related to the heart and blood vessels.")
    p.subheader("Services")
    p.write("-Heart checkups")
    p.write("-ECG")
    p.write("-Blood pressure monitoring")
    p.write("-Cardiac consultation")

    p.subheader("3. Pediatrics Department")
    p.image("ped.jfif")
    p.write("Provides medical care for infants, children, and teenagers.")
    p.subheader("Services")
    p.write("-growth monitoring")
    p.write("-fever treatment")
    p.write("-vaccinations")
    p.write("-Child health checkups")

    p.subheader("4.Neurology Department")
    p.image("nuo.jfif")
    p.write("Focuses on disorders affecting the brain, spinal cord, and nervous system.")
    p.subheader("Services")
    p.write("-nerve disorder treatment")
    p.write("-Neurological examinations")
    p.write("-headache evaluation")

    p.subheader("5. Radiology & Imaging")
    p.image("radp.jfif")
    p.write("Provides diagnostic imaging to help doctors identify and monitor medical conditions.")
    p.subheader("Services")
    p.write("-X-ray")
    p.write("-MRI")
    p.write("-ultrasound")

    p.subheader("Department Operating Days")
    qm = {"Emergency Departments": "Monday, Friday, Thurs",
          "Cardiology Department": "Thursday ",
          "Pediatrics Department": "Tuesday ",
          "Neurology Department" : "Wednesday,  -, -",
          "Radiology & Imaging": "Friday, Wednesday, Tuesday"}
    na = m.DataFrame(list(qm.items()), columns= ["Department", "Available Days"])


    p.table(na)

if aw == "Doctor List And Salary Analysis":
    p.header("Led by Experience, Driven by Care")
    p.subheader("Founded by Dr. U Myo Sat Paing")
    p.write("Our hospital is supported by a dedicated team of 5 Chief Doctors, 150+ professional nurses, and a wide range of healthcare and support staff. Together, our team works to provide reliable, compassionate, and high-quality care to every patient.")
    p.subheader("Meet Our Five Chief Doctors")

    v, j, s = p.columns(3)

    with v:
        p.image("Thura.png",
                caption= "Name: -Dr. Thura" )
        p.write("Specialization: Cardiology & Cardiovascular Medicine")
        p.write("Experience: 14 Years")
        p.write("Salary: $105,000 / year")
        p.write("Joined: April 15 -2013")
        p.write("End Date: December 2030")

    with j:
        p.image("Thae Su.png",
                caption= "Name: -Dr. Thae Su")
        p.write("Specialization: Pediatrics & Child Health")
        p.write("Experience: 18 Years")
        p.write("Salary: $108,977 / year")
        p.write("Joined: May 23 2013")
        p.write("End Date: September 19 2039")

    with s:
        p.image("d15c56be-f347-434d-ac31-f83dc26ae46e.png", 
                caption= "Name: Dr. Myo Thu")
        p.write("Specialization: Neurology & Brain Disorders")
        p.write("Experience: 16 Years")
        p.write("Salary: $123,890 / year")
        p.write("Joined: November 17 2011")
        p.write("End Date: September 29 2035")

    with v:
        p.image("d15c56be-f347-434d-ac31-f83dc26ae46e.png",
                caption= "Name: Dr. Khin OO")
        p.write("Specialization: General Surgery & Surgical Care")
        p.write("Experience: 14 Years")
        p.write("Salary: $103,894 / year")
        p.write("Joined:  September 18 2021")
        p.write("End Date: October 5 2030 ")

    with j:
        p.image(r"c:\Users\myosett\Desktop\My codes\Nyein Thu.png",
                 caption=" Name: Dr.Nyein Thu")
        p.write("Specialization: Orthopedics & Traumatology")
        p.write("Experience: 17 Years")
        p.write("Salary: $104,569 / year")
        p.write("Joined:  December 15 2020")
        p.write("End Date: June 14 2040 ")

    op = m.DataFrame({"Name": ["Dr.Nyein Thu", 
                               "Dr. Khin OO",
                                 "Dr. Myo Thu",
                                   "Dr. Thae Su", 
                                   "Dr. Thura"],

                      "Salary": [104,
                                  103,
                                    123,
                                      108,
                                        105],
                                        "Salary Profile": ["$104K/Year",
                                  "$103K/Year",
                                    "$123K/Year",
                                      "108K/Year",
                                        "105K/Year"],})

    
    aqp = q.Chart(op).mark_bar().encode(x= q.X("Name:N",
                                                 title= "Name"),
                                         y= q.Y("Salary:Q",
                                                 title= "Salary",
                                                 axis= q.Axis(labelExpr= "'$' + datum.value + 'K' + '' + '/Year'"), 
                                                 scale=  q.Scale(
                                                                  reverse= True
                                                                  , zero= False, 
                                                                  clamp= False
                                                            )), color= q.Color("Salary:Q"), 
                                                            tooltip= q.Tooltip("Salary Profile:N"))

    p.subheader("Salary Dashboard For Each Doctors")

    p.altair_chart(aqp)

    
if aw == "Our Location":
    mk = folium.Map(location= [16.7700435, 96.1605456], zoom_start= 60)

    pa = folium.Marker(location= [16.7700435, 96.1605456], 
                 
                                        popup= "Wow You Joined Us;)",
                            tooltip= "Our Hospital",
                              color = "pink", 
                              icon= folium.Icon(icon= "globe")
                              )
    pa.add_to(mk)
            
    am = st_folium(mk)

    p.subheader("Location: Near သစ်ထူးောင် စတိုး, 270 Strand Rd, Yangon")
   
with p.sidebar:
    p.link_button(label= "Log Out", url = "www.google.com")

        
        
    

    
