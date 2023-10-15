DROP TABLE IF EXISTS languages_list;

CREATE TABLE IF NOT EXISTS languages_list (
        languageId INTEGER PRIMARY KEY,
        languageName TEXT UNIQUE
    );

INSERT INTO languages_list(languageName)
VALUES('Adasen'),('Agta'),('Agta-Dumagat'),('Agusan Manobo'),('Agutaynen'),('Akeanon'),('Alangan'),('Ata'),('Ata-Manobo'),('Ayangan Ifugao'),('Ayta language group'),('Bagobo/Tagabawa'),('Balangao'),('Baliwon/Ga''dang'),('Banao'),('Bantoanon'),('Belwang (N.Bontok dialect)'),('Bikol'),('Binongan'),('Binukid'),('Bisaya/Binisaya'),('B''laan/Blaan language group'),('Bontok'),('Bugkalot/Ilongot'),('Buhid'),('Cagayanen'),('Capizeño'),('Cebuano'),('Chavacano'),('Cuyonon/Cuyonen'),('Davaweño'),('Dibabawon'),('Dumagat/Remontado'),('English'),('Gaddang'),('Giangan'),('Hanunuo'),('Higaonon'),('Hiligaynon Ilonggo'),('Ibaloi/Ibaloy'),('Ibanag'),('Ibatan'),('Ilianen Manobo'),('Ilocano'),('Iranun'),('Iraya'),('Isinai'),('Isnag'),('Itawis'),('Ivatan'),('Iwak/Iowak/Owak/I-wak'),('Jama Mapun'),('Kalagan'),('Kalanguya'),('Kalibugan/Kolibugan'),('Kalinga language group'),('Kamiguin'),('Kankanaey'),('Kapampangan'),('Karao'),('Karay-a'),('Kirenteken'),('Mabaka'),('Maeng'),('Maguindanao'),('Majokayong'),('Mamanwa'),('Mandaya'),('Manobo'),('Manobo-Cotabato'),('Mansaka'),('Maranao'),('Masadiit'),('Masbateño/Masbatenon'),('Matigsalog/Matigsalug'),('Molbog'),('Muyadan'),('Obo Manobo'),('Unspecified Sama language'),('Palawani'),('Palawano language group'),('Pangasinan/Panggalato'),('Paranan'),('Romblomanon'),('Sama Bangingi'),('Sama Laut'),('Sangil'),('Subanen/Subanon/Subanun'),('Surigaonon'),('Tadyawan'),('Tagakaulo'),('Tagalog'),('Tagbanua'),('Tagbanua Calamian'),('Tau-buid'),('Tausug'),('Tboli'),('Teduray'),('Tuwali'),('Waray'),('Yakan'),('Yogad'),('Zambal')
