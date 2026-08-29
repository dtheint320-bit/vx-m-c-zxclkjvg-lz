import mysql.connector
import streamlit as s
import hashlib


ye = mysql.connector.connect(host = "localhost",
                              user = "root",
                              password = "myogwin897",
                              database= "hospital")

n = ye.cursor()
n.execute("""CREATE TABLE if not exists hosp (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
     gender VARCHAR(20)
);""")
ye.commit()

mb, sc = s.tabs(["Create Account", "Login User"])

with mb:
    s.subheader("You Can Create Your Account Here")
    h = (s.text_input("Input Your Username"))
    w = (s.text_input("Input Your Password"))
    e = (s.text_input("Input Your Email"))
    fz = (s.selectbox("Choose Your Gendr", ["Male",
                                            "Female", 
                                            "Others"]))
    if s.checkbox("I agree to the Terms of Service and Privacy Policy, and I confirm that the information I have provided is accurate."):
        if s.button("Finish Verifying"):
            if h:
                if w:
                    if e:
                        if fz:
                            qw = hashlib.blake2b(w.encode("utf8"), digest_size= 18  
                                             
                                             )
                            m = hashlib.blake2b( 
                                             h.encode("utf8"),
                                             digest_size= 18)
                            v = hashlib.blake2b( 
                                             fz.encode("utf8"),
                                             digest_size= 5)
                            o = hashlib.blake2b( e.encode("utf8"), digest_size= 18
                                                                         
                                                                         
                                                                         )       
                            a = qw.hexdigest()
                            q = m.hexdigest()
                            z = v.hexdigest()
                            x = o.hexdigest()
                            mq = n.execute("""INSERT INTO hosp (username, email, password, gender)
                                    VALUES (%s,
                                      %s,
                                        %s,
                                          %s)""", 
                                          (q,
                                           x,
                                            a,
                                              z))
                            ye.commit()
                            
                            s.switch_page("pages/hospita.py")
                            s.success("Successfully Finisted About Verifying")
    
    else:
        if s.button("Finish Verifying"):
            pass

with sc:
    s.subheader("You Can Log In Here")
    wq = s.text_input("Set Your Email")
    k = s.text_input("Set Your Password")

    if s.checkbox("Access Your Aggreement "):
        if s.button("Finish Verifying", key= "dalkjfd"):
            if wq:
                if k:
                    dsa = hashlib.blake2b(wq.encode("utf8"),
                                            
                                             digest_size= 16)
                    qx = hashlib.blake2b(k.encode("utf8"), 
                                         digest_size= 16)

                    c = dsa.hexdigest()
                    aq = qx.hexdigest()

                    ea = n.execute("SELECT * FROM users WHERE email=%s AND password=%s",
    (c, aq))
                    qm = n.fetchone()

                    if qm:
                        s.success("You Successfully Log-in Your Account")
                        s.switch_page(r"c:\Users\myosett\hospita.py")
                    else:
                        s.warning("You Have No Registered")

                    

    


                        
                        
                        




