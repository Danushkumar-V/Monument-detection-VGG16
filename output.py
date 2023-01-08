import numpy as np
import streamlit as st



def printoutput(score):
    max = 0.0
    max_index = 0
    for i in range(0, len(score)):
        if(score[i] > max):    
            max = score[i]
            max_index = i  

     
    class_names = ['Ajanta Caves', 'Charar-E- Sharif', 'Chhota_Imambara', 'Ellora Caves', 'Fatehpur Sikri', 'Gateway of India', "Humayun's Tomb", 'India gate pics', 'Khajuraho', 'Sun Temple Konark', 'alai_darwaza', 'alai_minar', 'basilica_of_bom_jesus', 'charminar', 'golden temple', 'hawa mahal pics', 'iron_pillar', 'jamali_kamali_tomb', 'lotus_temple', 'mysore_palace', 'qutub_minar', 'tajmahal', 'tanjavur temple', 'victoria memorial']
    st.write(class_names[max_index])
    if class_names[np.argmax(score)] == "India gate pics":
        st.markdown('''
            # Monument name : **`India gate`**
            # Description : 
            '''
        )
        st.write('''`The India Gate (formerly known as the All India War Memorial) is a war memorial located astride the Rajpath, on the eastern edge of the "ceremonial axis" of New Delhi, formerly called Kingsway. It stands as a memorial to 90,000 soldiers of the British Indian Army who died in between 1914 and 1921 in the First World War, in France, 
        Flanders, Mesopotamia, Persia, East Africa, Gallipoli and elsewhere in the Near and the Far East, and the Third Anglo-Afghan War. 13,300 servicemen's names, including some soldiers and officers from the United Kingdom, are inscribed on the gate. Designed by Sir Edwin Lutyens, the gate evokes the architectural style of the memorial arch such as 
        the Arch of Constantine, in Rome, and is often compared to the Arc de Triomphe in Paris, and the Gateway of India in Mumbai.The India Gate was part of the work of the Imperial War Graves Commission (IWGC), which came into existence in December 1918 under the British rule for building war graves and memorials to soldiers who were killed in the First World War. The foundation stone of the gate then called the All India War Memorial, was laid on 10 February 1921, at 16:30, by the visiting Duke of Connaught in a ceremony attended by Officers and Men of the British Indian Army, Imperial Service Troops, the Commander in Chief, and Chelmsford, the viceroy. On the occasion, the viceroy is reported to have said, "The stirring tales of individual heroism, will live forever in the annals of this country", and that the memorial which was a tribute to the memory of heroes, "known and unknown", would inspire future generations to endure hardships with similar fortitude and "no less valour". The Duke also read out a message by the King, which said, "On this spot, in the central vista of the Capital of India, there will stand a Memorial Archway, designed to keep", in the thoughts of future generations, "the glorious sacrifice of the officers and men of the British Indian Army who fought and fell". During the ceremony, the Deccan Horse, 3rd Sappers and Miners, 6th Jat Light Infantry, 34th Sikh Pioneers, 39th Garhwal Rifles, 59th Scinde Rifles (Frontier Force), 117th Mahrattas, and 5th Gurkha Rifles (Frontier Force), were honoured with the title of "Royal" in recognition of the distinguished services and gallantry of the British Indian Army during the Great War.`

 `''')

        st.markdown(
            '''
            # Established : **`2/10/1921`**
            # Architect : **`Edwin Lutyens`**
            # Location : **`Rajpath, India Gate, New Delhi, Delhi 110001`**
            '''
        )
    elif class_names[np.argmax(score)] == "alai_darwaza":
        st.markdown('''
            # Monument name : **`Alai Darwaza`**
            # Description : 
            '''
        )
        st.write('''`Ala'i Darwaza (Urdu: علاء دروازه, lit. 'Gate of Alauddin') is the southern gateway of the Quwwat-ul-Islam Mosque in Qutb complex, Mehrauli,
        Delhi, India. Built by Sultan Alauddin Khalji in 1311 and made of red sandstone, it is a square domed gatehouse with arched entrances and houses a single chamber.
        It has a special significance in Indo-Islamic architecture as the first Indian monument to be built using Islamic methods of construction and ornamentation and is a World Heritage Site.The Alai Darwaza is made up of a single hall whose interior part measures 34.5 feet (10.5 m) and exterior part measures 56.5 feet (17.2 m). It is 60 feet (18 m) tall and the walls are 11 feet (3.4 m) thick.
The gatehouse, from 1311, still shows a cautious approach to the new technology, with very thick walls and a shallow dome, only visible from a certain distance or height. Bold contrasting colours of masonry, with red sandstone and white marble, introduce what was to become a common feature of Indo-Islamic architecture, substituting for the polychrome tiles used in Persia and Central Asia. The pointed arches come together slightly at their base, giving a mild horseshoe arch effect, and their internal edges are not cusped but lined with conventionalized "spearhead" projections, possibly representing lotus buds. Net, stone openwork screens, are introduced here; they already had been long used in temples.
The height of the dome is 47 feet (14 m). It is the first true dome built in India, as previous attempts to construct a true dome were not successful.
The entire Darwaza is made up of red sandstone with white coloured marbles inlaid on the exterior walls. There is extensive Arabic calligraphy on the walls of the Darwaza. The arches are horseshoe shaped, the first time such arches were used in India. The façade has pre-Turkish carvings and patterns. The windows have marble lattices. Surface decoration consists of interweaved floral tendrils and is repeated with a symmetry on three doorways.
`''')

        st.markdown(
            '''
            # Established : **`1311 AD`**
            # Architect : **`Ala-ud-Din Khalji`**
            # Location : **`Qutb Minar complex, Delhi, India`**
            '''
        )

    elif class_names[np.argmax(score)] == "alai_minar":
        st.markdown('''
            # Monument name : **`Alai Minar`**
            # Description : 
            '''
        )
        st.write('''`The Alai Minar is an incomplete monument that lies within the Qutb complex in South Delhi. Sultan Ala-ud-Din Khalji was an over ambitious Sultan of the Khilji dynasty and won many wars and battles.
        After a win from one of his Deccan campaigns, the Sultan dreamt of constructing a huge Tower or Minar to commemorate his victory. He wanted a structure that would double the height
        of Qutub Minar in order to be remembered as the only Sultan who dared to create such a monumental masterpiece that was grander and more spectacular than the Qutub Minar of Qutb-ud-din Aibak of the Slave dynasty that ruled before him.Alauddin Khalji started building the Alai Minar, after he had doubled the size of Quwwat ul-Islam mosque built before 1300AD. He conceived this tower to be two times higher than Qutb Minar in proportion with the enlarged mosque. The construction was however abandoned, just after the completion of the 25-metre-high (82 ft) first-story core; soon after the death of Alauddin in 1316, and never taken up by his successors of Khalji Dynasty. The first storey of the Alai Minar, a giant rubble masonry core, still stands today, which was evidently intended to be covered with dressed stone later on. Noted Sufi poet and saint of his times, Amir Khusro in his work, Tarikh-i-Alai, mentions Ala-ud-din's intentions to extend the mosque and also constructing another minar.`''')

        st.markdown(
            '''
            # Established : **`1316 AD`**
            # Architect : **`Alauddin Khilji`**
            # Location : **`Qutub Minar Complex Rd, Ladha Sarai, Mehrauli, New Delhi, Delhi 110030`**
            '''
        )
        
    elif class_names[np.argmax(score)] == "golden temple":
        st.markdown('''
            # Monument name : **`Golden Temple`**
            # Description : 
            '''
        )
        st.write('''`The Golden Temple (also known as the Harmandir Sahib, lit. 'abode of God', It is a gurdwara located in the city of Amritsar, Punjab, India. It is the preeminent spiritual site of Sikhism.
        The man-made pool on the site of the temple was completed by the fourth Sikh Guru, Guru Ram Das, in 1577.In 1604, Guru Arjan placed a copy of the Adi Granth in Harmandir Sahib.The Gurdwara was repeatedly rebuilt by 
        the Sikhs after it became a target of persecution and was destroyed several times by the Mughal, political parties and invading Afghan armies. Maharaja Ranjit Singh, after founding the Sikh Empire, rebuilt it in marble
        and copper in 1809, and overlaid the sanctum with gold leaf in 1830. This has led to the name the Golden Temple.The Golden Temple is spiritually the most significant shrine in Sikhism. It became a centre of the Singh Sabha Movement between 1883 and 1920s, and the Punjabi Suba movement between 1947 and 1966. In the early 1980s, the Gurdwara became a centre of conflict between the Indian government and a radical movement led by Jarnail Singh Bhindranwale. In 1984, Prime Minister Indira Gandhi sent in the Indian Army as part of Operation Blue Star, leading to deaths of over 1,000 soldiers and civilians, as well as causing much damage to the Gurdwara and the destruction of Akal Takht. The Gurdwara complex was rebuilt again after the 1984 damage.The Golden Temple is an open house of worship for all people, from all walks of life and faiths. It has a square plan with four entrances, and a circumambulation path around the pool. The four entrances to the temple symbolises the Sikh belief in equality and the Sikh view that all people are welcome into their holy place.The complex is a collection of buildings around the sanctum and the pool. One of these is Akal Takht, the chief centre of religious authority of Sikhism. Additional buildings include a clock tower, the offices of the Gurdwara Committee, a Museum and a langar – a free Sikh community–run kitchen that offers a vegetarian meal to all visitors without discrimination. Over 100,000 people visit the holy shrine daily for worship. The Gurdwara complex has been nominated as a UNESCO World Heritage Site, and its application is pending on the tentative list of UNESCO.
`''')

        st.markdown(
            '''
            # Established : **`1589 AD`**
            # Architect : **`Guru Ram Das, Guru Arjan`**
            # Location : **`Golden Temple Rd, Atta Mandi, Katra Ahluwalia, Amritsar, Punjab 143006`**
            '''
        )

    elif class_names[np.argmax(score)] == "hawa mahal pics":
        st.markdown('''
            # Monument name : **`Hawa Mahal `**
            # Description : 
            '''
        )
        st.write('''`The Hawa Mahal is a palace in the city of Jaipur, India. Built from red and pink sandstone,
        the palace sits on the edge of the City Palace, Jaipur, and extends to the Zenana, or women's chambers.
        The Hawa Mahal is a palace in the city of Jaipur, India. Built from red and pink sandstone, the palace sits on the edge of the City Palace, Jaipur,
        and extends to the Zenana, or women's chambers.The structure was built in 1799 by the Maharaja Sawai Pratap Singh, the grandson of Maharaja Sawai Jai Singh,
        who was the founder of the city of Jaipur, India.He was so inspired by the unique structure the of Khetri Mahal that he built this grand and historical palace.It was designed by Lal Chand Ustad. Its five-floor exterior is akin to a honeycomb with its 953 small windows called Jharokhas decorated with intricate latticework.The original intent of the lattice design was to allow royal ladies to observe everyday life and festivals celebrated in the street below without being seen, since they had to obey the strict rules of "purdah", which forbade them to appear in public without face coverings. This architectural feature also allowed cool air from the Venturi effect to pass through, thus making the whole area more pleasant during the high temperatures in summer.Many people see the Hawa Mahal from the street view and think it is the front of the palace, but it is the back.
In 2006, renovation works on the Mahal were undertaken, after a gap of 50 years, to give a facelift to the monument at an estimated cost of Rs 4.568  million. The corporate sector lent a hand to preserve the historical monuments of Jaipur and the Unit Trust of India has adopted Hawa Mahal to maintain it. The palace is an extended part of a huge complex. The stone-carved screens, small casements, and arched roofs are some of the features of this popular tourist spot. The monument also has delicately modelled hanging cornices.
This palace is a five-story pyramidal shaped monument that rises to about 50 feet (15 m). The top three floors of the structure have the width of a single room, while the first and second floors have patios in front of them. The front elevation, as seen from the street, is like a honeycomb with small portholes. Each porthole has miniature windows and carved sandstone grills, finials and domes. It gives the appearance of a mass of semi-octagonal bays, giving the monument its unique façade. The inner face on the back side of the building consists of chambers built with pillars and corridors with minimal ornamentation, and reach up to the top floor. The interior of the palace has been described as "having rooms of different coloured marbles, relieved by inlaid panels or gilding; while fountains adorn the centre of the courtyard".
Lal Chand Usta was the architect. Built-in red and pink coloured sandstone, in keeping with the décor of the other monuments in the city, its colour is a full testimony to the epithet of "Pink City" given to Jaipur. Its façade with 953 niches with intricately carved jharokhas (some are made of wood) is a stark contrast to the plain-looking rear side of the structure. Its cultural and architectural heritage is a reflection of a fusion of Hindu Rajput architecture and  Islamic Mughal architecture; the Rajput style is seen in the form of domed canopies, fluted pillars, lotus, and floral patterns, and the Islamic style as evident in its stone inlay filigree work and arches (as distinguished from its similarity with the Panch Mahal at Fatehpur Sikri).
The entry to the Hawa Mahal from the city palace side is through an imperial door. It opens into a large courtyard, which has double-storeyed buildings on three sides, with the Hawa Mahal enclosing it on the east side. An archaeological museum is also housed in this courtyard.
Hawa Mahal was also known as the chef-d'œuvre of Maharaja Jai Singh as it was his favourite resort because of the elegance and built-in interior of the Mahal. The cooling effect in the chambers, provided by the breeze passing through the small windows of the façade, was enhanced by the fountains provided at the centre of each of the chambers.
The top two floors of the Hawa Mahal are accessed only through ramps. The Mahal is maintained by the archaeological department of the Government of Rajasthan.
`''')

        st.markdown(
            '''
            # Established : **`1799`**
            # Architect : **`Pratap Singh of Jaipur, Lal Chand Ustad`**
            # Location : **`Hawa Mahal Rd, Badi Choupad, J.D.A. Market, Pink City, Jaipur, Rajasthan 302002`**
            '''
        )

    elif class_names[np.argmax(score)] == "iron_pillar":
        st.markdown('''
            # Monument name : **`Iron Pillar`**
            # Description : 
            '''
        )
        st.write('''`The iron pillar of Delhi is a structure 23 feet 8 inches (7.21 metres) high with a 16-inch (41 cm) diameter that was constructed by Chandragupta II (reigned c. 375–415 CE), and now stands in the Qutb complex at Mehrauli in Delhi, India.[1][2] It is famous for the rust-resistant composition of the metals used in its construction. The pillar weighs over three tonnes (6,614 lb) and is thought to have been erected elsewhere, perhaps outside the Udayagiri Caves,and moved to its present location by Anangpal Tomar in 11th century.The iron pillar in India was manufactured by the forge welding of pieces of wrought iron. In a report published in the journal Current Science, R. Balasubramaniam of the IIT Kanpur explains how the pillar's resistance to corrosion is due to a passive protective film at the iron-rust interface. The presence of second-phase particles (slag and unreduced iron oxides) in the microstructure of the iron, that of high amounts of phosphorus in the metal, and the alternate wetting and drying existing under atmospheric conditions are the three main factors in the three-stage formation of that protective passive film.
Lepidocrocite and goethite are the first amorphous iron oxyhydroxides that appear upon oxidation of iron. High corrosion rates are initially observed. Then, an essential chemical reaction intervenes: slag and unreduced iron oxides (second phase particles) in the iron microstructure alter the polarisation characteristics and enrich the metal–scale interface with phosphorus, thus indirectly promoting passivation of the iron] (cessation of rusting activity).
The second-phase particles act as a cathode, and the metal itself serves as anode, for a mini-galvanic corrosion reaction during environment exposure. Part of the initial iron oxyhydroxides is also transformed into magnetite, which somewhat slows down the process of corrosion. The ongoing reduction of lepidocrocite and the diffusion of oxygen and complementary corrosion through the cracks and pores in the rust still contribute to the corrosion mechanism from atmospheric conditions.
The next main agent to intervene in protection from oxidation is phosphorus, enhanced at the metal–scale interface by the same chemical interaction previously described between the slags and the metal. The ancient Indian smiths did not add lime to their furnaces. The use of limestone as in modern blast furnaces yields pig iron that is later converted into steel; in the process, most phosphorus is carried away by the slag.[39]
The absence of lime in the slag and the use of specific quantities of wood with high phosphorus content (for example, Cassia auriculata) during the smelting induces a higher phosphorus content (> 0.1%, average 0.25%) than in modern iron produced in blast furnaces (usually less than 0.05%). This high phosphorus content and particular repartition are essential catalysts in the formation of a passive protective film of misawite (d-FeOOH), an amorphous iron oxyhydroxide that forms a barrier by adhering next to the interface between metal and rust. Misawite, the initial corrosion-resistance agent, was thus named because of the pioneering studies of Misawa and co-workers on the effects of phosphorus and copper and those of alternating atmospheric conditions in rust formation.
`''')

        st.markdown(
            '''
            # Established : **`375–415 CE`**
            # Architect : **`Chandragupta II`**
            # Location : **`Mehrauli, New Delhi, Delhi 110030`**
            '''
        )    

    elif class_names[np.argmax(score)] == "jamali_kamali_tomb":
        st.markdown('''
            # Monument name : **`Jamali Kamali tomb `**
            # Description : 
            '''
        )
        st.write('''`Jamali Kamali Mosque and Tomb, located in the Archaeological Village complex in Mehrauli, Delhi, India, comprise two monuments adjacent to each other; one is the mosque and the other is the tomb of Jamali and Kamali. Their names are tagged together as "Jamali Kamali" for the mosque as well as the tomb since they are buried adjacent to each other. The mosque and the tomb were constructed in 1528-1529, and Jamali was buried in the tomb after his death in 1535.The Jamali Kamali mosque, positioned in an enclosed garden area, built first during the years 1528-29, has a southern entry. It is built in red sandstone with marble embellishments. It is claimed to be a forerunner in the design of Mughal mosque architecture in India. The prayer hall, fronted by a large courtyard, has five arches with the central arch only having a dome. The size of arches increases towards the central arch, which is the largest of the five arches embellished with beautiful ornamentation. The spandrels of the arch are decorated with medallions and ornamentation. Fluted pilasters exquisitely decorate the central arch. The prayer wall on the west has niches with mihrab. The niches and walls are decorated with a few Koranic inscriptions. A porch around the mosque provides access to the two storied mosque and the four corners are adorned by octagonal towers. The rear end of the mosque has been provided with oriel windows, apart from a small window on the central arch.[1]
 
The tomb of Jamali-Kamali is a decorated 7.6 m (25 ft) square structure with a flat roof, located adjacent to the mosque on its northern side. Inside the chamber, the flat ceiling is plastered and ornately decorated. It is painted in red and blue with some Koranic inscriptions, and the walls are adorned with inlaid coloured tiles inscribed with Jamali's poems. The decorations in the tomb have been described as giving the impression of "stepping into a jewel box". In the Jamali Kamali Mosque and Tomb the tomb chamber has two marble graves: one of Jamali, the saint poet and the other of Kamali. The reason for the Kamali name could probably be that it rhymes well with Jamali.
`''')

        st.markdown(
            '''
            # Established : **`1528`**
            # Architect : **`Saint Shaikh Fazlullah`**
            # Location : **`Mehrauli Archeological Park Trail, Christian Colony, Mehrauli, New Delhi, Delhi 110016`**
            '''
        )  

    elif class_names[np.argmax(score)] == "qutub_minar":
        st.markdown('''
            # Monument name : **`Qutub Minar `**
            # Description : 
            '''
        )
        st.write('''`The Qutub Minar, also spelled as Qutb Minar and Qutab Minar, is a minaret and "victory tower" that forms part of the Qutb complex, which lies at the site of Delhi’s oldest fortified city, Lal Kot, founded by the Tomar Rajputs. It is a UNESCO World Heritage Site in the Mehrauli area of South Delhi, India. It is one of most visited tourist spots in the city due to it being one of the earliest that survives in the Indian subcontinent.The Qutb Minar was built over the ruins of the Lal Kot, the citadel of Dhillika. Qutub Minar was begun after the Quwwat-ul-Islam Mosque, which was started around 1192 by Qutb-ud-din Aibak, first ruler of the Delhi Sultanate.
It is usually thought that the tower is named for Qutb-ud-din Aibak, who began it. It is also possible that it is named after Khwaja Qutbuddin Bakhtiar Kaki a 13th-century sufi saint, because Shamsuddin Iltutmish was a devotee of his.
The Minar is surrounded by several historically significant monuments of the Qutb complex. Quwwat-ul-Islam Mosque, to the north-east of the Minar was built by Qutub-ud-Din Aibak in A.D. 1198. It is the earliest extant - mosque built by the Delhi Sultans. It consists of a rectangular courtyard enclosed by cloisters, erected with the carved columns and architectural members of 27 Hindu and Jaina temples, which were demolished by Qutub-ud-Din Aibak as recorded in his inscription on the main eastern entrance. Later, a lofty arched screen was erected, and the mosque was enlarged, by Shams-ud- Din Itutmish (A.D. 1210-35) and Ala-ud-Din Khalji. The Iron Pillar in the courtyard bears an inscription in Sanskrit in Brahmi script of fourth century A.D., according to which the pillar was set up as a Vishnudhvaja (standard of god Vishnu) on the hill known as Vishnupada in memory of a mighty king named Chandra.
The mosque complex is one of the earliest that survives in the Indian subcontinent.
`''')

        st.markdown(
            '''
            # Established : **`1198`**
            # Architect : **`Qutb al-Din Aibak, Iltutmish, Firuz Shah Tughlaq, Sher Shah Suri, Sikandar Lodi`**
            # Location : **`Kalka Das Marg, Mehrauli, New Delhi - 110030`**
            '''
        )  

    elif class_names[np.argmax(score)] == "tajmahal":
        st.markdown('''
            # Monument name : **`Taj Mahal`**
            # Description : 
            '''
        )
        st.write('''`The Taj Mahal lit. 'Crown of the Palace',  is an ivory-white marble mausoleum on the right bank of the river Yamuna in the Indian city of Agra. It was commissioned in 1632 by the Mughal emperor Shah Jahan (r. 1628–1658) to house the tomb of his favourite wife, Mumtaz Mahal; it also houses the tomb of Shah Jahan himself. The tomb is the centrepiece of a 17-hectare (42-acre) complex, which includes a mosque and a guest house, and is set in formal gardens bounded on three sides by a crenellated wall.The uniqueness of Taj Mahal lies in some truly remarkable innovations carried out by the horticulture planners and architects of Shah Jahan. One such genius planning is the placing of tomb at one end of the quadripartite garden rather than in the exact centre, which added rich depth and perspective to the distant view of the monument. It is also, one of the best examples of raised tomb variety. The tomb is further raised on a square platform with the four sides of the octagonal base of the minarets extended beyond the square at the corners. The top of the platform is reached through a lateral flight of steps provided in the centre of the southern side. The ground plan of the Taj Mahal is in perfect balance of composition, the octagonal tomb chamber in the centre, encompassed by the portal halls and the four corner rooms. The plan is repeated on the upper floor. The exterior of the tomb is square in plan, with chamfered corners. The large double storied domed chamber, which houses the cenotaphs of Mumtaz Mahal and Shah Jahan, is a perfect octagon in plan. The exquisite octagonal marble lattice screen encircling both cenotaphs is a piece of superb workmanship. It is highly polished and richly decorated with inlay work. The borders of the frames are inlaid with precious stones representing flowers executed with wonderful perfection. The hues and the shades of the stones used to make the leaves and the flowers appear almost real. The cenotaph of Mumtaz Mahal is in perfect centre of the tomb chamber, placed on a rectangular platform decorated with inlaid flower plant motifs. The cenotaph of Shah Jahan is greater than Mumtaz Mahal and installed more than thirty years later by the side of the latter on its west. The upper cenotaphs are only illusory and the real graves are in the lower tomb chamber (crypt), a practice adopted in the imperial Mughal tombs.`''')

        st.markdown(
            '''
            # Established : **`1632`**
            # Architect : **`Ustad Ahmad Lahauri`**
            # Location : **`Agra, Uttar Pradesh, India`**
            '''
        )    

    elif class_names[np.argmax(score)] == "tanjavur temple":
        st.markdown('''
            # Monument name : **`Tanjavur temple`**
            # Description : 
            '''
        )
        st.write('''`Brihadeeswarar temple fire is a fire accident that occurred 
        during the consecration of the Brihadeeswarar Temple on 7 June 1997 in Thanjavur, 
        Tamil Nadu, India. The accident was caused by a spark that caught up the thatch.
        A stampede occurred due to the panic created, and a total of 48 people were killed 
        and left more than 200 people injured. It is believed a fire cracker lit near the temple 
        fell on the yagasala, a temporary structure built to accommodate the ritual ceremonies,
        and sparked the fire that spread to the thatched roofs. A stampede resulted when the panic-stricken devotees rushed the only entrance to the temple on the eastern side.Brihadeeshwara Temple (Peruvudaiyar Kovil) is a Hindu temple dedicated to Shiva located in Thanjavur in the Indian state of Tamil Nadu. It is also known as Periya Kovil, RajaRajeswara Temple and Rajarajesvaram. It is one of the largest temples in India and is an example of Dravidian architecture during the Chola period. Built by emperor Raja Raja Chola I and completed in 1010 AD, the temple turned 1000 years old in 2010. The temple is part of the UNESCO World Heritage Site known as the “Great Living Chola Temples”, with the other two being the Brihadeeswarar Temple, Gangaikonda Cholapuram and Airavatesvara temple.
The temple stands amidst fortified walls that were probably added in the 16th century. The vimanam (temple tower) is 216 ft (66 m) high and is the tallest in the world. The Kumbam (the apex or the bulbous structure on the top) of the temple is carved out of a single rock and weighs around 80 tons.
There is a big statue of Nandi (sacred bull), carved out of a single rock measuring about 16 ft (4.9 m) long and 13 ft (4.0 m) high at the entrance. The entire temple structure is made out of granite, the nearest sources of which are about 60 km to the west of temple. The temple is one of the most visited tourist attractions in Tamil Nadu.
`''')

        st.markdown(
            '''
            # Established : **`1010`**
            # Architect : **`Kunjara Mallan Raja Raja Perunthachan`**
            # Location : **`Membalam Rd, Balaganapathy Nagar, Thanjavur, Tamil Nadu 613007`**
            '''
        )

    elif class_names[np.argmax(score)] == "Ajanta Caves":
        st.markdown('''
            # Monument name : **`Ajanta Caves`**
            # Description : 
            '''
        )
        st.write('''`The Ajanta Caves are approximately 30 rock-cut Buddhist cave monuments dating from the 2nd century BCE to about 480 CE in the 
        Aurangabad district of Maharashtra state in India. The caves include paintings and rock-cut sculptures described as among the finest surviving
         examples of ancient Indian art, particularly expressive paintings that present emotions through gesture, pose and form.Ajanta Caves exemplifies one of the greatest achievements in ancient Buddhist rock-cut architecture. The artistic traditions at Ajanta present an important and rare specimen of art, architecture, painting, and socio-cultural, religious and political history of contemporary society in India. The development of Buddhism manifested through the architecture, sculptures, and paintings is unique and bears testimony to the importance of Ajanta as a major hub of such activities. Further, the epigraphic records found at Ajanta provide good information on the contemporary civilization.`''')

        st.markdown(
            '''
            # Established : **`480 CE`**
            # Architect : **`Buddhist monks`**
            # Location : **`Aurangabad District, Maharashtra State, India`**
            '''
        )
    elif class_names[np.argmax(score)] == "Champaner-Pavagadh Archaeological Park":
        st.markdown('''
            # Monument name : **`Champaner-Pavagadh Archaeological Park`**
            # Description : 
            '''
        )
        st.write('''`Champaner-Pavagadh Archaeological Park, a UNESCO World Heritage Site, is located in Panchmahal district in Gujarat,
         India. It is located around the historical city of Champaner, a city which was founded by Vanraj Chavda, the most prominent king 
         of the Chavda Dynasty, in the eighth century. He named it after the name of his friend and general Champa, also known later as Champaraj. 
         The heritage site is studded with forts with bastions starting from the hills of Pavagadh, and extending into the city of Champaner. 
         The park's landscape includes archaeological, historic and living cultural heritage monuments such as chalcolithic sites, a hill fortress 
         of an early Hindu capital, and remains of the 16th-century capital of the state of Gujarat. There are palaces, entrance gates and arches, mosques, 
         tombs and temples, residential complexes, agricultural structures and water installations such as stepwells and tanks, dating from the eighth to the 14th centuries. 
         The Kalika Mata Temple, located on top of the 800 metres (2,600 ft) high Pavagadh Hill, is an important Hindu shrine in the region, attracting large numbers of pilgrims throughout the year.
At the heart of Champaner, is the Citadel, whose most impressive features are its 16th-century monumental mosques (no longer used for worship), with their beautiful blending of Islamic and Hindu architecture. The huge Jami Masjid, just outside the Citadel’s east gate, boasts of a wonderful carved entrance porch that leads into a lovely courtyard surrounded by a pillared corridor. The prayer hall has two tall central minarets, further superb stone carving, multiple domes, finely latticed windows and seven mihrabs (prayer niches) along the back wall.
Other beautiful mosques include the Saher ki Masjid, behind the ticket office inside the Citadel, which was probably the private royal mosque, and the Kevda Masjid, 300m north of the Citadel and about 600m west of the Jami Masjid. Here you can climb narrow stairs to the roof, and higher up the minarets, to spot other mosques even further out into the countryside – Nagina Masjid, 500m north, with no minarets but exquisite geometric carving, particularly on the tomb next to it, and Lila Gumbaj ki Masjid, 800m east, on a high platform and with a fluted central dome. The twin minarets resembling factory chimneys, about 1 km west, adorn the Brick Minar ki Masjid, a rare brick tomb.
Brief History: Pavagadh became the capital of the Chauhan Rajputs around 1300, but in 1484 was taken by the Gujarat Sultan Mahmud Begada, after a 20-month siege; the Rajputs committed jauhar (ritual mass suicide) in the face of defeat. Following his capture of Pavagadh, Sultan Mahmud Begada turned Champaner, at the base of the hill, into a splendid new capital. But its glory was brief: when it was captured by Mughal emperor Humayun in 1535, the Gujarati capital reverted to Ahmedabad, and Champaner fell into ruin.
`''')

        st.markdown(
            '''
            # Established : **`1484`**
            # Architect : **`Sultan Mahmud Begadah`**
            # Location : **`Panchmahal district, Gujarat, India`**
            '''
        )

    elif class_names[np.argmax(score)] == "Ellora Caves":
        st.markdown('''
            # Monument name : **`Ellora Caves`**
            # Description : 
            '''
        )
        st.write('''`Ellora  is a UNESCO World Heritage Site located in the Aurangabad district of Maharashtra, 
        India. It is one of the largest rock-cut Hindu temple cave complexes in the world, with artwork dating from the period 600t to 1000 CE.
        Cave 16 features the largest single monolithic rock excavation in the world, the Kailash temple, a chariot-shaped monument dedicated to Lord Shiva. 
        The Kailash temple excavation also features sculptures depicting the gods, goddesses found in Hinduism as well as relief panels summarizing the two major Hindu EpicsThe most remarkable of the cave temples is Kailasa (Kailasanatha; cave 16), named for the mountain in the Kailas Range of the Himalayas where the Hindu god Shiva resides. Unlike other temples at the site, which were first delved horizontally into the rock face, the Kailasa complex was excavated downward from a basaltic slope and is therefore largely exposed to sunlight. Construction of the temple in the 8th century, beginning in the reign of Krishna I (c. 756–773), involved the removal of 150,000 to 200,000 tons of solid rock. The complex measures some 164 feet (50 metres) long, 108 feet (33 metres) wide, and 100 feet (30 metres) high and has four levels, or stories. It contains elaborately carved monoliths and halls with stairs, doorways, windows, and numerous fixed sculptures. One of its better-known decorations is a scene of Vishnu transformed into a man-lion and battling a demon. Just beyond the entrance, in the main courtyard, is a monument to Shiva’s bull Nandi. Along the walls of the temple, at the second-story level, are life-size sculptures of elephants and other animals. Among the depictions within the halls is that of the 10-headed demon king Ravana shaking Kailasa mountain in a show of strength. Erotic and voluptuous representations of Hindu divinities and mythological figures also grace the temple. Some features have been damaged or destroyed over the centuries, such as a rock-hewn footbridge that once joined two upper-story thresholds.`''')

        st.markdown(
            '''
            # Established : **`600–1000 CE`**
            # Architect : **`Rashtrakuta dynasty`**
            # Location : **`Aurangabad district, Maharashtra, India`**
            '''
        )
    elif class_names[np.argmax(score)] == "Fatehpur Sikri":
        st.markdown('''
            # Monument name : **`Fatehpur Sikri`**
            # Description : 
            '''
        )
        st.write('''`Fatehpur Sikri is a town in the Agra District of Uttar Pradesh, India.
         Situated 37 kms from the district headquarters Agra,[3] Fatehpur Sikri itself was founded
          as the capital of Mughal Empire in 1571 by Emperor Akbar, serving this role from 1571 to 1585,
           when Akbar abandoned it due to a campaign in Punjab and was later completely abandoned in 1610The inscribed property covers 60.735 ha, with a buffer zone of 475.542 ha. The city, which is bounded on three sides by a wall 6 km long fortified by towers and pierced by nine gates, includes a number of impressive edifices of secular and religious nature that exhibit a fusion of prolific and versatile Indo-Islamic styles. The city was originally rectangular in plan, with a grid pattern of roads and by-lanes which cut at right angles, and featured an efficient drainage and water management system. The well-defined administrative block, royal palaces, and Jama Masjid are located in the centre of the city. The buildings are constructed in red sandstone with little use of marble. Diwan-i-Am (Hall of Public Audience) is encircled by a series of porticos broken up at the west by the insertion of the emperor’s seat in the form of a small raised chamber separated by perforated stone screens and provided with pitched stone roof. This chamber communicates directly with the imperial palace complex clustered along a vast court. At the north side of it stands a building popularly known as Diwan-i-Khas (Hall of Private Audience), also known as the ‘Jewel House’. Other monuments of exceptional quality are Panch Mahal, an extraordinary, entirely columnar five-storey structure disposed asymmetrically on the pattern of a Persian badgir, or wind-catcher tower; the pavilion of Turkish Sultana; Anup Talao (Peerless Pool); Diwan-Khana-i-Khas and Khwabgah (Sleeping Chamber); palace of Jodha Bai, the largest building of the residential complex, which has richly carved interior pillars, balconies, perforated stone windows, and an azure-blue ribbed roof on the north and south sides; Birbal’s House; and the Caravan Sarai, Haram Sara, baths, water works, stables and Hiran tower. Architecturally, the buildings are a beautiful amalgamation of indigenous and Persian styles.`''')

        st.markdown(
            '''
            # Established : **`16th century`**
            # Architect : **`Emperor Akbar`**
            # Location : **`Agra, Uttar Pradesh, India`**
            '''
        )
    elif class_names[np.argmax(score)] == "Khajuraho":
        st.markdown('''
            # Monument name : **`Khajuraho`**
            # Description : 
            '''
        )
        st.write('''`The Khajuraho Group of Monuments are a group of Hindu and Jain temples in Chhatarpur district,
         Madhya Pradesh, India, about 175 kilometres southeast of Jhansi. They are a UNESCO World Heritage Site. 
         The temples are famous for their nagara-style architectural symbolism and less than 10% of their erotic sculpturesThe plan of the temples shows the spatial hierarchy of axially aligned interconnected spaces. The temples are entered through an ornate entrance porch (ardhamandapa), which leads to the main hall (mandapa), through which one accesses the vestibule (antarala) before reaching the sanctum (garbhagriha). The main halls of the temples were often accompanied by lateral transepts with projecting windows as well as a circumambulatory path around the sanctum. Larger temples had an additional pair of transepts and were accompanied by subsidiary shrines on the four corners of its jagati.
The temples of Khajuraho are known for the harmonious integration of sculptures with their architecture. All surfaces are profusely carved with anthropomorphic and non-anthropomorphic motifs depicting sacred and secular themes. Sculptures depicting acts of worship, clan and minor deities, and couples in union, all reflect the sacred belief system. Other themes mirror social life through depictions of domestic scenes, teachers and disciples, dancers and musicians, and amorous couples. The composition and finesse achieved by the master craftsmen give the stone surfaces of the Khajuraho temples a rare vibrancy and sensitivity to the warmth of human emotions.
`''')

        st.markdown(
            '''
            # Established : **`between 885 AD and 1050 AD`**
            # Architect : **`Chandela dynasty`**
            # Location : **`Khajuraho, Madhya Pradesh, India`**
            '''
        )
    elif class_names[np.argmax(score)] == "Pattadakal":
        st.markdown('''
            # Monument name : **`Pattadakal`**
            # Description : 
            '''
        )
        st.write('''`Pattadakal, also called Paṭṭadakallu or Raktapura, is a complex of 7th and 8th century CE Hindu and
         Jain temples in northern Karnataka (India). Located on the west bank of the Mallaprabha River in Bagalakote district,
          this UNESCO World Heritage Site[1][2] is 14 miles (23 km) from Badami and about 6 miles (9.7 km) from Aihole, both of
           which are historically significant centres of Chalukya monuments.[3][4] The monument is a protected site under Indian law
            and is managed by the Archaeological Survey of India (ASI)Home » Pattadakal » Pattadakal – The Temple Town
Pattadakal is situated on the banks of the Malaprabha River. The town is in Bagalkot district. Pattadakal is a testament to the architectural prowess of the Chalukya dynasty. The city was earlier called Pattada Kisuvolal, which translates to ‘City of Crown Rubies’.

There are 10 major temples in Pattadakal, all dedicated to Lord Shiva. The temples contain elements of both South Indian (Dravidian) and North Indian (Nagara) styles of architecture. The timeless beauty and historical relevance of these temples saw them acquire the status of a world heritage site in 1987.
Four temples are constructed in the traditional Dravidian style of architecture, with another 4 temples containing elements of Nagara architecture. The remaining two temples are a confluence of both architectural styles. The entire city resonates with the power of Shiva and draws several thousand tourists to it every year.
`''')

        st.markdown(
            '''
            # Established : **`10th century CE`**
            # Architect : **`Queen Loka Mahadevi`**
            # Location : **`Pattadakal, Karnataka, India`**
            '''
        )
    elif class_names[np.argmax(score)] == "Sun Temple Konark":
        st.markdown('''
            # Monument name : **`Sun Temple Konark`**
            # Description : 
            '''
        )
        st.write('''`Konark Sun Temple is a 13th-century CE (year 1250)
         Sun temple at Konark about 35 kilometres (22 mi) northeast from Puri city on the coastline in Puri district, Odisha,
          India. The temple is attributed to king Narasimhadeva I of the Eastern Ganga dynasty about 1250 CE.`''')

        st.markdown(
            '''
            # Established : **`1250 CE`**
            # Architect : **`king Narasimhadeva`**
            # Location : **`Konark, Odisha, India`**
            '''
        )
    elif class_names[np.argmax(score)] == "Humayun's Tomb":
        st.markdown('''
            # Monument name : **`Humayun's Tomb`**
            # Description : 
            '''
        )
        st.write('''`Humayun’s Tomb, Delhi is the first of the grand dynastic mausoleums that were 
        to become synonyms of Mughal architecture with the architectural style reaching its zenith 
        80 years later at the later Taj Mahal. Humayun’s Tomb stands within a complex of 27.04 ha.
         that includes other contemporary, 16th century Mughal garden-tombs such as Nila Gumbad, 
         Isa Khan, Bu Halima, Afsarwala, Barber’s Tomb and the complex where the craftsmen employed
          for the Building of Humayun’s Tomb stayed, the Arab Serai.A UNESCO World Heritage site, Konark Sun Temple is famous for its unique architecture. Its geometrical patterns and carved wheels used to serve as sun dials. One can witness three images of Sun God at three directions to catch the rays of the Sun at dawn, noon and sunset.`''')

        st.markdown(
            '''
            # Established : **`1570`**
            # Architect : **`Akbar`**
            # Location : **`Mathura road, Nizamuddin East, Delhi, India`**
            '''
        )
    elif class_names[np.argmax(score)] == "lotus_temple":
        st.markdown('''
            # Monument name : **`Lotus Temple`**
            # Description : 
            '''
        )
        st.write('''`The Lotus Temple, located in Delhi, India, is a Baháʼí House of Worship 
        that was dedicated in December 1986. Notable for its flowerlike shape, it has become 
        a prominent attraction in the city. Like all other Bahá’í Houses of Worship, 
        the Lotus Temple is open to all, regardless of religion or any other qualification.All Baháʼí Houses of Worship, including the Lotus Temple, share certain architectural elements, some of which are specified by Baháʼí scripture. ʻAbdu'l-Bahá, the son of the founder of the religion, stipulated that an essential architectural character of a House of Worship is a nine-sided circular shape. While all current Baháʼí Houses of Worship have a dome, this is not regarded as an essential part of their architecture. Baháʼí scripture also states that no pictures, statues or images be displayed within the House of Worship and no pulpits or altars be incorporated as an architectural feature (readers may stand behind simple portable lecture stands.
Inspired by the lotus flower, the design for the House of Worship in New Delhi is composed of 27 free-standing marble-clad "petals" arranged in clusters of three to form nine sides. The nine doors of the Lotus Temple open onto a central hall 34.3 meters tall that can seat 1,300 people and hold up to 2,500 in all. The surface of the House of Worship is made of white marble from Penteli mountain in Greece, the same marble used in the construction of many ancient monuments (including the Parthenon) and other Baháʼí buildings. Along with its nine surrounding ponds and gardens, the Lotus Temple property comprises 26 acres (105,000 m²; 10.5 ha).
Lotus temple is situated near Okhla NSIC and Kalkaji Mandir metro station is just 500 meters away.
The temple is located in the village of Bahapur in New Delhi, National Capital Territory of Delhi. The architect was an Iranian, Fariborz Sahba who now lives in La Jolla, California, after living some years in Canada. He was approached in 1976 to design the Lotus Temple and later oversaw its construction. The structural design was undertaken by the UK firm Flint and Neill over the course of 18 months, and the construction was done by ECC Construction Group of Larsen & Toubro Limited at a cost of $10 million. The major part of the funds needed to buy this land was donated by Ardishír Rustampúr of Hyderabad, Sindh (Pakistan), whose will dictated that his entire life savings would go to this purpose. A portion of the construction budget was saved and used to build a greenhouse to study indigenous plants and flowers that would be appropriate for use on the site.
Of the temple's total electricity use of 500 kilowatts (kW), 120 kW is provided by solar power generated by solar panels on the building. This saves the temple ₹120,000 per month. It is the first temple in Delhi to use solar power.
`''')

        st.markdown(
            '''
            # Established : **`1986`**
            # Architect : **`Fariborz Sahba`**
            # Location : **`Lotus Temple Rd, Bahapur, Shambhu Dayal Bagh, Kalkaji, New Delhi, Delhi 110019`**
            '''
        )
    elif class_names[np.argmax(score)] == "mysore_palace":
        st.markdown('''
            # Monument name : **`Mysore palace`**
            # Description : 
            '''
        )
        st.write('''`The Mysore Palace, also known as Amba Vilas Palace, is a historical palace and a royal residence. 
        It is located in Mysore, Karnataka. It used to be the official residence of the Wadiyar dynasty and the seat of 
        the Kingdom of Mysore. The palace is in the centre of Mysore, and faces the Chamundi Hills eastward.The architectural style of domes of the palace is commonly described as Indo-Saracenic, with blends of the Hindu, Mughal, Rajput, and Gothic styles. It is a three-storey stone structure with marble domes, and has a 145-foot five-storey tower. The palace is surrounded by a large garden. The entrance gate and arch hold the emblem and coat of arms of the kingdom of Mysore, around which the kingdom's motto is written in Sanskrit: "न बिभॆति कदाचन" (never terrified).
The main complex is 245 ft long and 156 ft wide. There are fire extinguishing machines located in all parts of the palace in order to prevent any fires. The palace has three entrances: the east gate (the front gate, opened only during the Dasara and for dignitaries), the south entrance (for the public), and the west entrance (usually opened only during the Dasara).[citation needed]
The three-storey stone building of a fine grey granite with deep pink marble domes has a facade with several expansive arches and two smaller ones flanking the central arch, which is supported by tall pillars. Above the central arch is a sculpture of Gajalakshmi, the goddess of wealth, prosperity, fortune, and abundance, with her elephants. There are three major exclusive temple buildings within the Old Fort, and about 18 inside the central palace building. The palace was built adjacent to the even older Parakala Mutt headquarters, whose leaders have remained the rajagurus (royal teacher and guide) of Mysore kings. The kings of Mysore were devotees of Goddess Chamundi, hence the palace faces the Chamundi Hills.The palace houses two durbar halls(ceremonial meeting halls of the royal court) and incorporates an array of courtyards, gardens, and buildings.
Apart from it's outstanding architecture, the palace is also known for it's impeccable roof art, tiles nad mosaics, paintings of the royal family and festive possessions. There also lies display rooms containing old cannons and rifles used by the imperial army, as well as mounted ivory, sandalwood and pearl boxes, as well as granite carvings of animals.
`''')

        st.markdown(
            '''
            # Established : **`1912`**
            # Architect : **`Maharani Pramoda Devi Wadiyar`**
            # Location : **`Sayyaji Rao Rd, Agrahara, Chamrajpura, Mysuru, Karnataka 570001`**
            '''
        )
    elif class_names[np.argmax(score)] == "Victoria Memorial":
        st.markdown('''
            # Monument name : **`Victoria Memorial`**
            # Description : 
            '''
        )
        st.write('''`The Victoria Memorial is a large marble building in Central Kolkata,
         which was built between 1906 and 1921. It is dedicated to the memory of Queen Victoria,
          now a museum under the auspices of the Ministry of Culture, and is the largest monument in the 
          world which is dedicated to a royal.In January 1901, on the death of Queen Victoria, then Lord Curzon, suggested the creation of a fitting memorial. Lord Curzon proposed the construction of a grand building with a museum and gardens.
Curzon said,
"Let us, therefore, have a building, stately, spacious, monumental and grand, to which every newcomer in Calcutta will turn, to which all the resident population, European and Native, will flock, where all classes will learn the lessons of history and see revived before their eyes the marvels of the past."The Prince of Wales, laid the foundation stone on 4 January 1906, and it was formally opened to the public in 1921.
In 1912, before the construction of the Victoria Memorial was finished, King George V announced the transfer of the capital of India from Kolkata to New Delhi. Thus, the Victoria Memorial was built in what would be a provincial city rather than a capital.
The Victoria Memorial was mainly funded by British officials and individuals of India.The politicians and people of India responded generously to Lord Curzon's appeal for funds, and the total cost of construction of the monument, amounting to one crore, five lakhs of Rupees (₹), was entirely derived from their voluntary subscriptions.The construction of the Victoria Memorial was delayed by Curzon's departure from India in 1905 with a subsequent loss of local enthusiasm for the project and the need for testing of the foundations. The Victoria Memorial's foundation stone was set in 1906 and the building opened in 1921.The work of construction was entrusted to Messrs. Martin & Co. of Kolkata. Work on the superstructure began in 1910. After 1947, some additions were made to the Memorial.
A smaller Victoria memorial was also constructed in the Hardoi District, which has since been converted into a city club for recreation. It is also where Mahatma Gandhi addressed Hardoi in the 1930's.

`''')

        st.markdown(
            '''
            # Established : **`1921`**
            # Architect : **`William Emerson, Vincent Esch`**
            # Location : **`Victoria Memorial Hall, 1, Queens Way, Maidan, Kolkata, West Bengal 700071`**
            '''
        )
    elif class_names[np.argmax(score)] == " Gateway of India":
        st.markdown('''
            # Monument name : **` Gateway of India`**
            # Description : 
            '''
        )
        st.write('''`The Gateway of India is an arch-monument built in the early 20th century in the city of Mumbai, India.
         It was erected to commemorate the landing of King-Emperor George V, the first British monarch to visit India, 
         in December 1911 at Ramchandani Road near Shyamaprasad Mukherjee Chowk.The foundation stone was laid in March 1913 for a monument built in the Indo-Saracenic style, incorporating elements of 16th-century Gujarati architecture. The final design of the monument by architect George Wittet was sanctioned only in 1914, and construction was completed in 1924. The structure is a memorial arch made of basalt, which is 26 metres (85 feet) high, with an architectural resemblance to a triumphial arch as well as Gujarati architecture of the time.
After its construction the Gateway was used as a symbolic ceremonial entrance to India for important colonial personnel. The Gateway is also the monument from where the last British troops left India in 1948, following Indian independence. It is located on the waterfront at an angle, opposite the Taj Mahal Palace and Tower Hotel and overlooks the Arabian Sea. Today, the monument is synonymous with the city of Mumbai, and is amongst its prime tourist attractions. The gateway is also a gathering spot for locals, street vendors, and photographers soliciting services. It holds significance for the local Jewish community as it has been the spot for Hanukkah celebrations, with the lighting of the menorah, since 2003. There are five jetties located at the Gateway, of which two are used for commercial ferry operations.
The Gateway was the site of a terror attack in August 2003, when there was a bomb blast in a taxi parked in front of it. Access to the gateway was restricted after people congregated at its premises following the 2008 Mumbai terror attacks, in which the Taj Hotel opposite the gateway and other locations in its vicinity were targeted.
In March 2019, the Maharashtra state government proposed a four-step plan to develop the location for the convenience of tourists, following a direction issued by the state governor in February 2019.
`''')

        st.markdown(
            '''
            # Established : **`1924`**
            # Architect : **`George Wittet`**
            # Location : **`Apollo Bandar, Colaba, Mumbai, Maharashtra 400001`**
            '''
        )


    elif class_names[np.argmax(score)] == "basilica_of_bom_jesus":
        st.markdown('''
            # Monument name : *`Basilica of Bom Jesus`*
            # Description : 
            '''
        )
        st.write('''`The Basilica of Bom Jesus is a Roman Catholic basilica located in the Goa state, situated in the Konkan region of India. It is both a pilgrimage centre and also the most iconic monument of all the churches and convents of Goa, recognised by UNESCO as a World Heritage Site.Construction work on the church began in 1594. The church was consecrated in May 1605 by the archbishop, Dom Fr. Aleixo de Menezes. This world heritage monument has emerged as a landmark in the history of Christianity. It contains the body of St. Francis Xavier, a very close friend of St. Ignatius Loyola with whom he founded the Society of Jesus (the Jesuits). Francis Xavier died on Sancian Island, Chuandao (川島鎮), Taishan while en route to continental China on (3 December 1552). It is also believed that the body is of Ven. Thotagamuwe Sri Rahula Thera, a Sri Lankan Buddhist monk.
The body of Francis Xavier was first taken to [Portuguese Malacca] and two years later shipped back to Goa. It is said that the saint's body was as fresh as the day it was buried. The remains of the saint still attract a huge number of tourists (Christian and non-Christian alike) from all over the world, especially during the public viewing of his body every ten years (last held in 2014). The saint is said to have miraculous powers of healing.
This is one of the oldest churches in Goa and in India. The floor is of marble inlaid with precious stones. Apart from the elaborate gilded altars, the interior of the church is simple. The main altar holds a large statue of St. Ignatius of Loyola, the founder of the Society of Jesus (Jesuits), and one of Francis Xavier's companions whose words drew him to a reformed life. "What does it profit a man," Ignatius had asked Francis, "if he gains the whole world and loses his soul?"
The gaze of the gilded statue of Ignatius of Loyola is fixed upwards in awe at the name of Jesus (IHS) on the gilded emblem of the Jesuits, encircled in radiant rays. Over the emblem, is the Holy Trinity -Father, Son and Spirit - the ultimate muse and focus of the pious Christian. The altar table which is used in Holy mass is gilded and adorned with the figures of Christ and his apostles at the Last Supper, along with the words "Hi Mhoji Kudd", which in Konkani means "This is my Body", from the Institution Narrative.
The church also holds paintings of scenes taken from the life of St. Francis Xavier. The mausoleum, on the top of which is placed the silver casket with the body of St. Francis Xavier (1696), was the gift of the last of the Medicis, Cosimo III, the Grand Duke of Tuscany.
The mausoleum was designed by the 17th-century Florentine sculptor Giovanni Battista Foggini. It took ten years to complete. The casket containing his body is made of silver. The holy relics of the saint are displayed every ten years during the anniversary of the saint's death. His liturgical feast is 3 December.
On the upper level, overlooking the tomb is the Bom Jesus Basilica Art Gallery, containing the works of the Goan surrealist painter, Dom Martin. Author and fellow Jesuit Anthony De Mello was also from Goa and mentions the basilica in his writings.
The Basilica of Bom Jesus is more than 408 years old and is open to the public every day. The body of St. Francis Xavier is in a well-decorated casket, which can be seen in the photographs below. Solemn exhibitions of the 'body' are held every ten years. Some photos taken inside the church are attached for better understanding of the artwork of that time. These artworks are called "murals".
`''')

        st.markdown(
            '''
            # Established : *`1605`*
            # Architect : *`Fr. Alexia de Menezes`*
            # Location : *`Old Goa Road, Bainguinim, Goa 403402`*
            '''
        )

    elif class_names[np.argmax(score)] == "Charar-E- Sharif":
            st.markdown('''
                # Monument name : *`Charar E Sharif`*
                # Description : 
                '''
        )
            st.write('''`Charar-i-Sharief in Kashmiri, is a town and a notified area committee in Budgam district in the Indian union territory of Jammu and Kashmir, India. The town was given the status of block in January 2014. The town is divided into 10 wards. Each ward has a municipal councillor.The famous mohallas of Charar-i-Sharief are: Talab-e-Kalan or Bada Talab, Trajibal, Court Road, Gulshanabad, Nowhar, Baghi Noor U Din Nowhar, Jabl-e-Noor, Wazabagh, Alamdar colony, Zaloosa and Kumar Mohalla.
Charar-i-Sharief is considered one of the most sacrosanct Muslim shrines in Kashmir. It is situated approximately 28 km (17 mi) from Srinagar, en route to Yusmarg. The Shrine of Charar-i-Sharief is approximately 600 years old. It is popularly known as the "Sheikh Noor-ud-Din Wali".
`''')

            st.markdown(
                '''
                # Established : *`1460`*
                # Architect : *`Zain-ul-Abidin`*
                # Location : *`Charar-i-Sharief-Srinagar Rd, Charar-i-Sharief 191112`*
                '''
            )


    elif class_names[np.argmax(score)] == "charminar":
            st.markdown('''
                # Monument name : *`Charminar`*
                # Description : 
                '''
            )
            st.write('''`The Charminar is a monument located in Hyderabad, Telangana, India. The landmark has become known globally as a symbol of Hyderabad and is listed among the most recognised structures in India. It has also been officially incorporated as the Emblem of Telangana.The fifth ruler of the Qutb Shahi dynasty, Muhammad Quli Qutb Shah, built the Charminar in 1591 after shifting his capital from Golkonda to the newly formed city of Hyderabad.
The Archaeological Survey of India (ASI), the current caretaker of the structure, mentions in its records, "There are various theories regarding the purpose for which Charminar was constructed. However, it is widely accepted that Charminar was built at the centre of the city, to commemorate the eradication of plague", a deadly disease which was wide spread at that time. According to Jean de Thévenot, a French traveller of the 17th century whose narration was complemented with the available Persian texts, the Charminar was constructed in the year 1591 CE, to commemorate the beginning of the second Islamic millennium year (1000 AH). The event was celebrated far and wide in the Islamic world, thus Qutb Shah founded the city of Hyderabad to celebrate the event and commemorate it with the construction of this building. Due to its architecture it is also called as Arc de Triomphe of the east.[11]
The Charminar was constructed at the intersection of the historical trade route that connects the city to international markets through the port city of Machilipatnam. The Old City of Hyderabad was designed with Charminar as its centrepiece.The city was spread around the Charminar in four different quadrants and chambers, segregated according to the established settlements. Towards the north of Charminar is the Char Kaman, or four gateways, constructed in the cardinal direction. Additional eminent architects from Persia were also invited to develop the city plan. The structure itself was intended to serve as a mosque and madrasa. It is of Indo-Islamic architecture style, incorporating Persian architectural elements. A sample of Charminar is said to have been created at Dabirpura/Nagaboli graveyard before the actual construction.
Historian Masud Hussain Khan says that the construction of Charminar was completed in the year 1592, and that it is the city of Hyderabad which was actually founded in the year 1591. According to the book "Days of the Beloved", Qutb shah constructed the Charminar in the year 1589, on the very spot where he first glimpsed his future queen Bhagmati, and after her conversion to Islam, Qutb Shah renamed the city as "Hyderabad". Though the story was rejected by the historians and scholars, it became popular folklore among the locals.
`''')

            st.markdown(
                '''
                # Established : *`1837 AD`*
                # Architect : *`Imambara`*
                # Location : *`Husainabad Trust Rd, Tahseen Ganj, Husainabad, Lucknow, Uttar Pradesh 226003`*
                '''
            )


    elif class_names[np.argmax(score)] == "Chhota_imambara":
            st.markdown('''
                # Monument name : *``*
                # Description : 
                '''
            )
            st.write('''`Chota Imambara, also known as Imambara Hussainabad Mubarak is an imposing monument located in the city of Lucknow, Uttar Pradesh, India. It took 54 years to finalize it. Built as an imambara or a congregation hall for Shia Muslims, by Muhammad Ali Shah, the Nawab of Awadh in 1838,[1] it was to serve as a mausoleum for himself and his mother, who is buried beside him.The significance of Panjetan, the holy five, is once again emphasized here with five main doorways. This Imambara consist of two halls and a Shehnasheen (a platform where the Zarih of Imam Husain is kept.) Zarih is the replica of that protective grill or structure which is kept on the grave of Imam Husain at Karbala, Iraq. The large green and white bordered hall of Azakhana is richly decorated with chandeliers and a good number of crystal glass lamp-stands. In fact, it was for this profuse decoration that the Imambara was referred by European visitors and writers as The Palace of Lights. The exterior is very beautifully decorated with Quranic verses in Islamic calligraphy .It is situated near the Bara Imambara and on the connecting road stands an imposing gateway known as Rumi Darwaza.The building is also known as the Palace of Lights because of its decorations and chandeliers during special festivals, like Muharram.
The chandeliers used to decorate the interior of this building were brought from Belgium. Also housed within the building, is the crown of Muhammad Ali Shah and ceremonial tazias. Thousands of labourers worked on the project to gain famine relief.
It has a gilded dome and several turrets and minarets. The tombs of Muhammad Ali Shah and other members of his family are inside the imambara. This includes two replicas of the Taj Mahal, built as the tombs of Muhammad Ali Shah's daughter and her husband. The walls are decorated with Arabic calligraphy.
Water supply for the fountains and the water bodies inside the imambara came directly from the Gomti River.
`''')

            st.markdown(
                '''
                # Established : *`1837 AD`*
                # Architect : *`Imambara`*
                # Location : *`Husainabad Trust Rd, Tahseen Ganj, Husainabad, Lucknow, Uttar Pradesh 226003`*
                '''
            )




    elif  np.argmax(score)<=0.1:
        st.text("No such class is defined!")


