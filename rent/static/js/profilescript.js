// $(document).ready(function(){
    
//     $('#contactform').on('click', 'button#emailbutton', function(event){
//         event.preventDefault();
//         $.ajax("{% url '/contact/success' %}",{
//             beforeSend: function(){
//                 $('#status').text('Sending Email..');
//             }
//         })
//         .done(function(response){
//             $('#htmlinfo').html(response);
//         })
//         .always(function(){
//             $('#status').text('Done!');
//         });
//     });
// });
function sendingemail(){
    var x = document.getElementById("statussendingemail");
    x.style.visibility='visible';
}


function getdis(){
    var x = document.getElementById("district");
    var wardno = document.getElementById("wardno");
    var province = document.getElementById("province").value;
    var dis;
    switch(province){
        case `Province 1`:
            dis = ["Bhojpur", "Dhankuta", "Ilam","Jhapa","Khotang","Morang","Okhaldhunga","Panchthar","Sankhuwasabha","Solukhumbu","Sunsari","Taplejung","Terhathum","Udayapur"];
            break;
        case `Province 2`:
            dis = ["Bara","Parsa","Dhanusha","Mahottari","Rautahat","Saptari","Sarlahi","Siraha"];
            break;
        case `Bagmati Pradesh`:
            dis = ["Bhaktapur","Chitwan","Dhading","Dolakha","Kathmandu","Kavrepalanchok","Lalitpur","Makwanpur","Nuwakot","Ramechhap","Rasuwa","Sindhuli","Sindhupalchok"];
            break;
        case `Gandaki Pradesh`:
            dis = ["Baglung","Gorkha","Kaski","Lamjung","Manang","Mustang","Myagdi","Nawalpur","Parbat","Syangja","Tanahun"];
            break;
        case `Province 5`:
            dis = ["Arghakhanchi","Banke","Bardiya","Dang","EasternRukum","Gulmi","Kapilvastu","Parasi","Palpa","Pyuthan","Rolpa","Rupandehi"];
            break;
        case `Karnali Pradesh`:
            dis = ["Dailekh","Dolpa","Humla","Jajarkot","Jumla","Kalikot","Mugu","Salyan","Surkhet","WesternRukum"];
            break;
        case `Sudurpashchim Pradesh`:
            dis = ["Achham","Baitadi","Bajhang","Bajura","Dadeldhura","Darchula","Doti","Kailali","Kanchanpur"];
            break;
        default:
            console.log("Please select a province.");
    }    
    let dist_options = dis.map(d => `<option value="${d}">${d}</option>`).join('\n');
    x.innerHTML = dist_options;
    getmun()
}
function getmun(){
    var x = document.getElementById("municipality");
    x.style.visibility='visible';
    var mun;
    let mun_options;
    var dist = document.getElementById("district").value;
    dis = ["Bhojpur", "Dhankuta", "Ilam","Jhapa","Khotang","Morang","Okhaldhunga","Panchthar","Sankhuwasabha","Solukhumbu","Sunsari","Taplejung","Terhathum","Udayapur"];
    switch($.trim(dist)){
        case "Bhojpur":
            mun = ["Bhojpur Municipality","Shadanand Municipality", "Hatuwagadhi Rural Municipality","Ramprasad Rai Rural Municipality","Aamchok Rural Municipality","Tyamke Maiyunm Rural Municipality","Arun Rural Municipality","Pauwadungma Rural Municipality","Salpasilichho Rural Municipality"];
            break;
        case "Dhankuta":
            mun = ["Pakhribas Municipality","Dhankuta Municipality","Mahalaxmi Municipality", "Sangurigadhi Rural Municipality","Khalsa Chhintang Sahidbhumi Rural Municipality","Chhathar Jorpati Rural Municipality","Chaubise Rural Municipality"];
            break;
        case "Ilam":
            mun = ["Ilam Municipality","Deumai Municipality","Mai Municipality","Suryodaya Municipality", "Phakphokthum Rural Municipality","Chulachuli Rural Municipality","Maijogmai Rural Municipality","Mangsebung Rural Municipality","Rong Rural Municipality","Sandakpur Rural Municipality"];
            break;
        case "Jhapa":
            mun = ["Mechinagar Municipality","Damak Municipality","Kankai Municipality","Bhadrapur Municipality","Arjundhara Municipality","Shivasatakshi Municipality","Gauradaha Municipality","Birtamod Municipality","Kamal Rural Municipality","Gaurigunj Rural Municipality","Barhadashi Rural Municipality","Jhapa Rural Municipality","Buddhashanti Rural Municipality","Haldibari Rural Municipality","Kachankawal Rural Municipality"];
            break;
        case "Khotang":
            mun = ["Rupakot Majhuwagadhi Municipality","Halesi Tuwachung Municipality", "Khotehang Rural Municipality","Diprung Rural Municipality","Aiselukharka Rural Municipality","Jantedhunga Rural Municipality","Kepilasgadhi Rural Municipality","Barahpokhari Rural Municipality","Lamidanda Rural Municipality","Sakela Rural Municipality"];
            break;
        case "Morang":
            mun = ["Biratnagar Metropolitan City", "Belbari Municipality","Letang Municipality","Pathari Sanischare Municipality","Rangeli Municipality","Ratuwamai Municipality","Sunawarshi Municipality","Urlabari Municipality","Sundar Haraicha Municipality", "Budhiganga Rural Municipality","Dhanpalthan Rural Municipality","Gramthan Rural Municipality","Jahada Rural Municipality","Kanepokhari Rural Municipality","Katahari Rural Municipality","Kerabari Rural Municipality","Miklajung Rural Municipality"];
            break;
        
        case "Okhaldhunga":
            mun = ["Siddhicharan Municipality", "Manebhanjyang Rural Municipality","Champadevi Rural Municipality","Sunkoshi Rural Municipality","Molung Rural Municipality","Chisankhugadhi Rural Municipality","Khiji Demba Rural Municipality","Likhu Rural Municipality"];
            break;
        case "Panchthar":
            mun = ["Phidim Municipality", "Phalelung Rural Municipality","Phalgunanda Rural Municipality","Hilihang Rural Municipality","Kummayak Rural Municipality","Miklajung Rural Municipality","Tumbewa Rural Municipality","Yangwarak Rural Municipality"];
            break;
        
        case "Sankhuwasabha":
            mun = ["Chainpur Municipality","Dharmadevi Municipality","Khandbari Municipality","Madi Municipality","Panchkhapan Municipality", "Bhotkhola Rural Municipality","Chichila Rural Municipality","Makalu Rural Municipality","Sabhapokhari Rural Municipality","Silichong Rural Municipality"];
            break;
        
        case "Solukhumbu":
            mun = ["Solududhkunda Municipality", "Dudhakaushika Rural Municipality","Necha Salyan Rural Municipality","Dudhkoshi Rural Municipality","Maha Kulung Rural Municipality","Sotang Rural Municipality","Khumbu Pasang Lhamu Rural Municipality","Likhu Pike Rural Municipality"];
            break;
        case "Sunsari":
            mun = ["Itahari Sub-Metropolitan City","Dharan Sub-Metropolitan City", "Inaruwa Municipality","Duhabi Municipality","Ramdhuni Municipality","Barahachhetra Municipality", "Koshi Rural Municipality","Gadhi Rural Municipality","Barju Rural Municipality","Bhokraha Rural Municipality","Harinagara Rural Municipality","Dewanganj Rural Municipality"];
            break;
        case "Taplejung":
            mun = ["Phungling Municipality", "Aathrai Triveni Rural Municipality","Sidingwa Rural Municipality","Fatthanglung Rural Municipality","Mikkwakhola Rural Municipality","Meringden Rural Municipality","Maiwakhola Rural Municipality","Pathibhara Yangwarak Rural Municipality","Sirijangha Rural Municipality"];
            break;
        case "Terhathum":
            mun = ["Myanglung Municipality","Laligurans Municipality", "Aathrai Rural Municipality","Chhathar Rural Municipality","Phedap Rural Municipality","Menchayayem Rural Municipality"];
            break;
        
        case "Udayapur":
            mun = ["Triyuga Municipality","Chaudandigadhi Municipality","Belaka Municipality","Katari Municipality", "Udayapurgadhi Rural Municipality","Rautamai Rural Municipality","Limchungbung Rural Municipality","Tapli Rural Municipality"];
            break;
        
        case "Bara":
            mun = ["Jeetpur Simara Sub-Metropolitan City","Kalaiya Sub-Metropolitan City", "Kolhabi Municipality","Nijgadh Municipality","Mahagadhimai Municipality","Simraungadh Municipality","Pacharauta Municipality", "Pheta Rural Municipality","Bishrampur Rural Municipality","Prasauni Rural Municipality","Adarsh Kotwal Rural Municipality","Karaiyamai Rural Municipality","Devtal Rural Municipality","Parwanipur Rural Municipality","Baragadhi Rural Municipality","Suwarna Rural Municipality"];
            break;

        case "Parsa":
            mun = ["Birgunj Metropolitan City", "Bahudarmai Municipality","Parsagadhi Municipality","Pokhariya Municipality","Bindabasini Rural Municipality","Chhipaharmai Rural Municipality","Jagarnathpur Rural Municipality","Jirabhawani Rural Municipality","Kalikamai Rural Municipality","Pakaha Mainpur Rural Municipality","Paterwa Sugauli Rural Municipality","Sakhuwa Prasauni Rural Municipality","Thori Rural Municipality"];
            break;
        case "Dhanusha":
            mun = ["Janakpur Sub-Metropolitan City","Chhireshwarnath Municipality","Ganeshman Charanath Municipality","Dhanusadham Municipality","Nagarain Municipality","Bideha Municipality","Mithila Municipality","Sahidnagar Municipality","Sabaila Municipality","Kamala Municipality","Mithila Bihari Municipality","Hansapur Municipality", "Janaknandani Rural Municipality","Bateshwar Rural Municipality","Mukhiyapatti Musharniya Rural Municipality","Lakshminya Rural Municipality","Aurahi Rural Municipality","Dhanauji Rural Municipality"];
            break;
        case "Mahottari":
            mun = ["Aurahi Municipality","Balawa Municipality","Bardibas Municipality","Bhangaha Municipality","Gaushala Municipality","Jaleshwor Municipality","Loharpatti Municipality","Manara Shiswa Municipality","Matihani Municipality","Ramgopalpur Municipality", "Ekdara Rural Municipality","Mahottari Rural Municipality","Pipara Rural Municipality","Samsi Rural Municipality","Sonama Rural Municipality"];
            break;
        case "Rautahat":
            mun = ["Baudhimai Municipality","Brindaban Municipality","Chandrapur Municipality","Dewahi Gonahi Municipality","Gadhimai Municipality","Garuda Municipality","Gaur Municipality","Gujara Municipality","Ishanath Municipality","Katahariya Municipality","Madhav Narayan Municipality","Maulapur Municipality","Paroha Municipality","Phatuwa Bijayapur Municipality","Rajdevi Municipality","Rajpur Municipality", "Durga Bhagwati Rural Municipality","Yamunamai Rural Municipality"];
            break;
        case "Saptari":
            mun = ["Bodebarsain Municipality","Dakneshwori Municipality","Hanumannagar Kankalini Municipality","Kanchanrup Municipality","Khadak Municipality","Sambhunath Municipality","Saptakoshi Municipality","SurungaRajbiraj Municipality","Agnisaira Krishnasavaran Rural Municipality","Balan-Bihul Rural Municipality","Rajgadh Rural Municipality","Bishnupur Rural Municipality","Chhinnamasta Rural Municipality","Mahadeva Rural Municipality","Rupani Rural Municipality","Tilathi Koiladi Rural Municipality","Tirhut Rural Municipality"];
            break;
        case "Sarlahi":
            mun = ["Bagmati Municipality","Balara Municipality","Barahathwa Municipality","Godaita Municipality","Harion Municipality","Haripur Municipality","Haripurwa Municipality","Ishworpur Municipality","Kabilasi Municipality","Lalbandi Municipality","Malangwa Municipality", "Basbariya Rural Municipality","Bishnu Rural Municipality","Brahampuri Rural Municipality","Chakraghatta Rural Municipality","Chandranagar Rural Municipality","Dhankaul Rural Municipality","Kaudena Rural Municipality","Parsa Rural Municipality","Ramnagar Rural Municipality"];
            break;
        case "Siraha":
            mun = ["Lahan Municipality","Dhangadhimai Municipality","Siraha Municipality","Golbazar Municipality","Mirchaiya Municipality","Kalyanpur Municipality","Karjanha Municipality","Sukhipur Municipality","Bhagwanpur Rural Municipality","Aurahi Rural Municipality","Bishnupur Rural Municipality","Bariyarpatti Rural Municipality","Lakshmipur Patari Rural Municipality","Naraha Rural Municipality","Sakhuwanankar Katti Rural Municipality","Arnama Rural Municipality","Navarajpur Rural Municipality"];
            break;
        case "Bhaktapur":
            mun = ["Bhaktapur Municipality","Changunarayan Municipality","Madhyapur Thimi Municipality","Suryabinayak Municipality"];
            break;
        case "Chitwan":
            mun = ["Bharatpur Metropolitan City", "Ratnanagar Municipality","Khairhani Municipality","Kalika Municipality","Rapti Municipality","Madi Municipality", "Ichchhakamana Rural Municipality"];
            break;
        case "Dhading":
            mun = ["Dhunibesi Municipality","Nilkantha Municipality", "Khaniyabas Rural Municipality","Gajuri Rural Municipality","Galchhi Rural Municipality","Gangajamuna Rural Municipality","Jwalamukhi Rural Municipality","Thakre Rural Municipality","Netrawati Dabjong Rural Municipality","Benighat Rorang Rural Municipality","Ruby Valley Rural Municipality","Siddhalek Rural Municipality","Tripurasundari Rural Municipality"];
            break;
        case "Dolakha":
            mun = ["Bhimeshwar Municipality","Jiri Municipality", "Kalinchok Rural Municipality","Melung Rural Municipality","Bigu Rural Municipality","Gaurishankar Rural Municipality","Baiteshwor Rural Municipality","Sailung Rural Municipality","Tamakoshi Rural Municipality"];
            break;
        case "Kathmandu":
            mun = ["Kathmandu Metropolitan City", "Budanilkantha Municipality","Chandragiri Municipality","Dakshinkali Municipality","Gokarneshwar Municipality","Kageshwari Manohara Municipality","Kirtipur Municipality","Nagarjun Municipality","Shankharapur Municipality","Tarakeshwar Municipality","Tokha Municipality"];
            break;
        case "Kavrepalanchok":
            mun = ["Dhulikhel Municipality","Banepa Municipality","Panauti Municipality","Panchkhal Municipality","Namobuddha Municipality","Mandandeupur Municipality","Khani Khola Rural Municipality","Chauri Deurali Rural Municipality","Temal Rural Municipality","Bethanchok Rural Municipality","Bhumlu Rural Municipality","Mahabharat Rural Municipality","Roshi Rural Municipality"];
            break;
        case "Lalitpur":
            mun = ["Lalitpur Metropolitan City","Mahalaxmi Municipality","Godawari Municipality","Konjyoson Rural Municipality","Bagmati Rural Municipality","Mahankal Rural Municipality"];
            break;
        case "Makwanpur":
            mun = ["Hetauda Sub-Metropolitan City", "Thaha Municipality", "Bhimphedi Rural Municipality","Makawanpurgadhi Rural Municipality","Manahari Rural Municipality","Raksirang Rural Municipality","Bakaiya Rural Municipality","Bagmati Rural Municipality","Kailash Rural Municipality","Indrasarowar Rural Municipality"];
            break;
        case "Nuwakot":
            mun = ["Bidur Municipality","Belkotgadhi Municipality","Kakani Rural Municipality","Panchakanya Rural Municipality","Likhu Rural Municipality","Dupcheshwar Rural Municipality","Shivapuri Rural Municipality","Tadi Rural Municipality","Suryagadhi Rural Municipality","Tarkeshwar Rural Municipality","Kispang Rural Municipality","Myagang Rural Municipality"];
            break;
        case "Ramechhap":
            mun = ["Manthali Municipality","Ramechhap Municipality", "Likhu Rural Municipality","Umakunda Rural Municipality","Khandadevi Rural Municipality","Doramba Rural Municipality","Gokulganga Rural Municipality","Sunapati Rural Municipality"];
            break;
        case "Rasuwa":
            mun = ["Kalika Rural Minicipality","Gosaikunda Rural Municipality","Naukunda Rural Municipality","Parbatikunda Rural Minicipality","Uttargaya Rural Municipality"];
            break;
        case "Sindhuli":
            mun = ["Kamalamai Municipality","Dudhauli Municipality","Sunkoshi Rural Municipality","Hariharpur Gadhi Rural Municipality","Tinpatan Rural Municipality","Marin Rural Municipality","Golanjor Rural Municipality","Phikkal Rural Municipality","Ghyanglekh Rural Municipality"];
            break;
        case "Sindhupalchok":
            mun = ["Chautara Sangachowkgadhi Municipality","Bahrabise Municipality","Melamchi Municipality", "Balephi Rural Municipality","Sunkoshi Rural Municipality","Indrawati Rural Municipality","Jugal Rural Municipality","Panchpokhari Thangpal Rural Municipality","Bhotekoshi Rural Municipality","Lisankhu Pakhar Rural Municipality","Helambu Rural Municipality","Tripurasundari Rural Municipality"];
            break;
        case "Baglung":
            mun = ["Baglung Municipality","Dhorpatan Municipality","Galkot Municipality","Jaimuni Municipality","Bareng Rural Municipality","Kanthekhola Rural Municipality","Taman Khola Rural Municipality","Tara Khola Rural Municipality","Nisikhola Rural Municipality","Badigad Rural Municipality"];
            break;
        case "Gorkha":
            mun = ["Gorkha Municipality","Palungtar Municipality", "Sulikot Rural Municipality","Siranchok Rural Municipality","Ajirkot Rural Municipality","Chum Nubri Rural Municipality","Dharche Rural Municipality","Bhimsen Rural Municipality","Sahid Lakhan Rural Municipality","Aarughat Rural Municipality","Gandaki Rural Municipality"];
            break;
        case "Kaski":
            mun = ["Pokhara Metropolitan City", "Annapurna Rural Municipality","Machhapuchchhre Rural Municipality","Madi Rural Municipality","Rupa Rural Municipality"];
            break;
        case "Lamjung":
            mun = ["Besisahar Municipality","Rainas Municipality","Sundarbazar Municipality","Madhya Nepal Municipality","Dordi Rural Municipality","Dudhpokhari Rural Municipality","Kwhlosothar Rural Municipality","Marsyandi Rural Municipality"];
            break;
        case "Manang":
            mun = ["Chame Rural Municipality","Nashon Rural Municipality","Narpa Bhumi Rural Municipality","Manang Ngisyang Rural Municipality"];
            break;
        case "Mustang":
            mun = ["Gharpajhong Rural Municipality","Thasang Rural Municipality","Baragung Muktichhetra Rural Municipality","Lomanthang Rural Municipality","Dalome Rural Municipality"];
            break;
        case "Myagdi":
            mun = ["Beni Municipality","Annapurna Rural Municipality","Dhaulagiri Rural Municipality","Mangala Rural Municipality","Malika Rural Municipality","Raghuganga Rural Municipality"];
            break;
        case "Nawalpur":
            mun = ["Kawasoti Municipality","Gaindakot Municipality","Devachuli Municipality","Madhyabindu Municipality","Bungdikali Rural Municipality","Bulingtar Rural Municipality","Binayi Tribeni Rural Municipality","Hupsekot Rural Municipality"];
            break;
        case "Parbat":
            mun = ["Kushma Municipality","Phalewas Municipality","Jaljala Rural Municipality","Paiyun Rural Municipality","Mahashila Rural Municipality","Modi Rural Municipality","Bihadi Rural Municipality"];
            break;
        case "Syangja":
            mun = ["Bhirkot Municipality","Chapakot Municipality","Galyang Municipality","Putalibazar Municipality","Waling Municipality","Aandhikhola Rural Municipality","Arjun Chaupari Rural Municipality","Biruwa Rural Municipality","Fedikhola Rural Municipality","Harinas Rural Municipality","Kaligandaki Rural Municipality"];
            break;
        case "Tanahun":
            mun = ["Bhanu Municipality","Bhimad Municipality","Byas Municipality","Shuklagandaki Municipality","Anbu Khaireni Rural Municipality","Devghat Rural Municipality","Bandipur Rural Municipality","Rhishing Rural Municipality","Ghiring Rural Municipality","Myagde Rural Municipality"];
            break;
        case "Arghakhanchi":
            mun = ["Sandhikharka Municipality","Sitganga Municipality","Bhumikasthan Municipality","Chhatradev Rural Municipality","Panini Rural Municipality","Malarani Rural Municipality"];
            break;
        case "Banke":
            mun = ["Nepalgunj Sub-Metropolitan City","Kohalpur Municipality","Rapti-Sonari Rural Municipality","Narainapur Rural Municipality","Duduwa Rural Municipality","Janaki Rural Municipality","Khajura Rural Municipality","Baijanath Rural Municipality"];
            break;
        case "Bardiya":
            mun = ["Gulariya Municipality","Rajapur Municipality","Madhuwan Municipality","Thakurbaba Municipality","Basgadhi Municipality","Barbardiya Municipality","Badhaiyatal Rural Municipality","Geruwa Rural Municipality"];
            break;
        case "Dang":
            mun = ["Ghorahi Sub-Metropolitan City","Tulsipur Sub-Metropolitan City","Lamahi Municipality","Gadhawa Rural Municipality","Rajpur Rural Municipality","Shantinagar Rural Municipality","Rapti Rural Municipality","Banglachuli Rural Municipality","Dangisharan Rural Municipality","Babai Rural Municipality"];
            break;
        case $.trim("EasternRukum"):
            mun = ["Putha Uttarganga Rural Municipality","Bhume Rural Municipality","Sisne Rural Municipality"];
            break;
        case "Gulmi":
            mun = ["Musikot	Municipality","Resunga Municipality", "Chatrakot Rural Municipality","Dhurkot Rural Municipality","Gulmidarbar Rural Municipality","Isma Rural Municipality","Kaligandaki Rural Municipality","Madane Rural Municipality","Malika Rural Municipality","Ruru Rural Municipality", "Satyawati Rural Municipality"];
            break;
        case "Kapilvastu":
            mun = ["Kapilvastu Municipality","Banganga Municipality","Buddhabhumi Municipality","Shivaraj Municipality","Krishnanagar Municipality","Maharajgunj Municipality","Mayadevi Rural Municipality","Yashodhara Rural Municipality","Suddhodhan Rural Municipality","Bijaynagar Rural Municipality"];
            break;
        case "Parasi":
            mun = ["Bardghat Municipality","Ramgram Municipality","Sunwal Municipality", "Susta Rural Municipality","Palhi Nandan Rural Municipality","Pratappur Rural Municipality","Sarawal Rural Municipality"];
            break;
        case "Palpa":
            mun = ["Tansen Municipality","Rampur Municipality","Rainadevi Chhahara Rural Municipality","Ripdikot Rural Municipality","Bagnaskali Rural Municipality","Rambha Rural Municipality","Purbakhola Rural Municipality","Nisdi Rural Municipality","Mathagadi Rural Municipality","Tinahu Rural Municipality"];
            break;
        case "Pyuthan":
            mun = ["Sworgadwary Municipality", "Pyuthan Municipality","Ayirabati Rural Municipality","Gaumukhi Rural Municipality","Jhimruk Rural Municipality","Mallarani Rural Municipality","Mandavi Rural Municipality","Naubahini Rural Municipality", "Sarumarani Rural Municipality", "Sworgadwary Rural Municipality"];
            break;
        case "Rolpa":
            mun = ["Rolpa Municipality","Runtigadi Rural Municipality","Triveni Rural Municipality","Sunil Smiriti Rural Municipality","Lungri Rural Municipality","Sunchhari Rural Municipality","Thawang Rural Municipality","Madi Rural Municipality","Ganga Dev Rural Municipality","Pariwartan Rural Municipality"];
            break;
        case "Rupandehi":
            mun = ["Butwal Sub-Metropolitan City", "Devdaha Municipality","Lumbini Sanskritik Municipality","Sainamaina Municipality","Siddharthnagar Municipality","Tilottama Municipality", "Gaidahawa Rural Municipality","Kanchan Rural Municipality","Kotahimai Rural Municipality","Marchbari Rural Municipality","Mayadevi Rural Municipality","Omsatiya Rural Municipality","Rohini Rural Municipality","Sammarimai Rural Municipality","Siyari Rural Municipality","Suddodhan Rural Municipality"];
            break;
        case "Dailekh":
            mun = ["Narayan Municipality","Dullu Municipality","Aathbis Municipality","Chamunda Bindrasaini Municipality","Thantikandh Rural Municipality","Bhairabi Rural Municipality","Mahabu Rural Municipality","Naumule Rural Municipality","Dungeshwar Rural Municipality","Gurans Rural Municipality","Bhagawatimai Rural Municipality"];
            break;
        case "Dolpa":
            mun = ["Thuli Bheri Municipality","Tripura Sundari Municipality","Dolpo Buddha Rural Municipality","She Phoksundo Rural Municipality","Jagadulla Rural Municipality","Mudkechula Rural Municipality","Kaike Rural Municipality","Chharka Tangsong Rural Municipality"];
            break;
        case "Humla":
            mun = ["Simkot Rural Municipality","Namkha Rural Municipality","Kharpunath Rural Municipality","Sarkegad Rural Municipality","Chankheli Rural Municipality","Adanchuli Rural Municipality","Tanjakot Rural Municipality"];
            break;
        case "Jajarkot":
            mun = ["Bheri Municipality","Chhedagad Municipality","Nalgad Municipality", "Barekot Rural Municipality","Kushe Rural Municipality","Junichande Rural Municipality","Shivalaya Rural Municipality"];
            break;
        case "Jumla":
            mun = ["Chandannath Municipality","Kankasundari Rural Municipality","Sinja Rural Municipality","Hima Rural Municipality","Tila Rural Municipality","Guthichaur Rural Municipality","Tatopani Rural Municipality","Patarasi Rural Municipality"];
            break;
        case "Kalikot":
            mun = ["Khandachakra Municipality","Raskot Municipality","Tilagufa Municipality","Pachaljharana Rural Municipality","Sanni Triveni Rural Municipality","Narharinath Rural Municipality","Shubha Kalika Rural Municipality","Mahawai Rural Municipality","Palata Rural Municipality"];
            break;
        case "Mugu":
            mun = ["Chhayanath Rara Municipality", "Mugum Karmarong Rural Municipality","Soru Rural Municipality","Khatyad Rural Municipality"];
            break;
        case "Salyan":
            mun = ["Shaarda Municipality","Bagchaur Municipality","Bangad Kupinde Municipality","Kalimati Rural Municipality","Tribeni Rural Municipality","Kapurkot Rural Municipality","Chhatreshwori Rural Municipality","Siddha Kumakh Rural Municipality","Kumakh Rural Municipality","Darma Rural Municipality"];
            break;
        case "Surkhet":
            mun = ["Birendranagar Municipality","Bheriganga Municipality","Gurbha Kot Municipality","Panchapuri Municipality","Lekbesi Municipality","Chaukune Rural Municipality","Barahatal Rural Municipality","Chingad Rural Municipality","Simta Rural Municipality"];
            break;
        case "WesternRukum":
            mun = ["Musikot Municipality","Chaurjahari Municipality","Aathbiskot Municipality","Banphikot Rural Municipality","Tribeni Rural Municipality","Sani Bheri Rural Municipality"];
            break;
        case "Achham":
            mun = ["Mangalsen Municipality","Kamalbazar Municipality","Sanphebagar Municipality","Panchadeval Binayak Municipality","Chaurpati Rural Municipality","Mellekh Rural Municipality","Bannigadi Jayagad Rural Municipality","Ramaroshan Rural Municipality","Dhukari Rural Municipality","Turmakhand Rural Municipality"];
            break;
        case "Baitadi":
            mun = ["Dasharathchand Municipality","Patan Municipality","Melauli Municipality","Purchaudi Municipality","Sunarya Rural Municipality","Sigas Rural Municipality","Shivanath Rural Municipality","Pancheshwor Rural Municipality","Dogdakedar Rural Municipality","Dilasaini Rural Municipality"];
            break;
        case "Bajhang":
            mun = ["Jayaprithvi Municipality","Bungal Municipality","Talkot Rural Municipality","Masta Rural Municipality","Khaptadchhanna Rural Municipality","Thalara Rural Municipality","Bitthadchir Rural Municipality","Surma Rural Municipality","Chhabispathivera Rural Municipality","Durgathali Rural Municipality","Kedarsyu Rural Municipality","Kanda Rural Municipality"];
            break;
        case "Bajura":
            mun = ["Badimalika Municipality","Triveni Municipality","Budhiganga Municipality","Budhinanda Municipality", "Gaumul Rural Municipality","Pandav Gufa Rural Municipality","Swamikartik Rural Municipality","Chhededaha Rural Municipality","Himali Rural Municipality"];
            break;
        case "Dadeldhura":
            mun = ["Amargadhi Municipality","Parshuram Municipality", "Aalital Rural Municipality","Bhageshwor Rural Municipality","Navadurga Rural Municipality","Ajayameru Rural Municipality","Ganyapadhura Rural Municipality"];
            break;
        case "Darchula":
            mun = ["Mahakali Municipality","Shailyashikhar Municipality","Malikarjun Rural Municipality","Apihimal Rural Municipality","Duhun Rural Municipality","Naugadh Rural Municipality","Marma Rural Municipality","Lekam Rural Municipality","Byans Rural Municipality"];
            break;
        case "Doti":
            mun = ["Dipayal Silgadhi Municipality","Shikhar Municipality","Purbichauki Rural Municipality","Badikedar Rural Municipality","Jorayal Rural Municipality","Sayal Rural Municipality","Aadarsha Rural Municipality","Kisingh Rural Municipality","Bogatan Rural Municipality"];
            break;
        case "Kailali":
            mun = ["Dhangadhi Sub-Metropolitan City", "Tikapur Municipality","Ghodaghodi Municipality","Lamkichuha Municipality","Bhajani Municipality","Godawari Municipality","Gauriganga Municipality","Janaki Rural Municipality","Bardgoriya Rural Municipality","Mohanyal Rural Municipality","Kailari Rural Municipality","Joshipur Rural Municipality","Chure Rural Municipality"];
            break;
        case "Kanchanpur":
            mun = ["Bhimdatta Municipality","Punarbas Municipality","Bedkot Municipality","Mahakali Municipality","Shuklaphanta Municipality","Belauri Municipality","Krishnapur Municipality","Beldandi Rural Municipality","Laljhadi Rural Municipality"];
            break;
        
        default:
            mun = ["something went wrong","Please contatact us","via Email","Thank you"];
            break;
    }
    mun_options = mun.map(d => `<option value="${d}">${d}</option>`).join('\n');
    x.innerHTML = mun_options;
}
