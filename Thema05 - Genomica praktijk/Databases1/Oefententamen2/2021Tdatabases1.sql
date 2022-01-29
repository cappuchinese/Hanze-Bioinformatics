drop table if exists scientists;
drop table if exists alignments;
drop table if exists querysequences;
drop table if exists experiments;

create table querysequences(
    id          varchar(10)     not null unique,
    sequence    varchar(200),

    primary key(id)
);

create table experiments(
    id          int             not null unique,
    datum       date            null,
    program     varchar(100)    not null,
    matrix      varchar(100)    not null,
    evalue      double          not null,
    maxgaps     int             null,
    dbase       varchar(100)    not null,

    primary key(id)
);

create table alignments(
    id          int             not null unique auto_increment,
    query       varchar(10)     not null,
    experiment  int             not null,
    evalue      double          not null,
    score       int,
    identity    int,
    externalid  varchar(200),

    constraint fk_al_exp foreign key(experiment) references experiments(id) on delete restrict,
    constraint fk_al_qs foreign key(query) references querysequences(id) on delete restrict,
    primary key(id)
);

create table scientists(
	id			int				not null unique auto_increment,
	title		char(3)			null,
	fam_name	char(50)		null,
	initials	char(3)			not null,
	experiment	int				not null,
	
	constraint fk_sci_exp foreign key(experiment) references experiments(id) on delete restrict,
	primary key(id)
);

insert into querysequences values('prot_1', 'MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH');
insert into experiments (id, program, matrix, evalue, maxgaps, dbase) values (1499, 'blastp', 'BLOSUM62', 3.47458e-98, 11, 'nr');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.21164e-104, 771, 147, 'gi|60833497|gb|AAX37051.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.30835e-104, 771, 147, 'gi|60653727|gb|AAX29557.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.69825e-104, 770, 147, 'gi|4504349|ref|NP_000509.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 5.93759e-104, 767, 146, 'gi|232230|sp|P02024.2|HBB_GORGO');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 6.34531e-104, 766, 146, 'gi|256028940|gb|ACU56984.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 6.34531e-104, 766, 146, 'gi|26892090|gb|AAN84548.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 6.34531e-104, 766, 146, 'gi|71727231|gb|AAZ39780.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 8.27083e-104, 766, 146, 'gi|4378804|gb|AAD19696.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.22627e-103, 764, 146, 'gi|229752|pdb|1COH|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.63095e-103, 764, 146, 'gi|6003534|gb|AAF00489.1|AF181989_1');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.36578e-103, 763, 145, 'gi|169791771|pdb|2YRS|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.47856e-103, 761, 145, 'gi|442850|pdb|1DXU|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.59522e-103, 761, 145, 'gi|1431650|pdb|1HDB|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.71571e-103, 761, 145, 'gi|442854|pdb|1DXV|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.23856e-103, 761, 145, 'gi|161760892|pdb|2DXM|D');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.33774e-103, 761, 146, 'gi|18418633|gb|AAL68978.1|AF083883_1');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.99458e-103, 760, 145, 'gi|46014946|pdb|1NQP|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.99458e-103, 760, 145, 'gi|27065154|pdb|1K1K|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 7.92875e-103, 759, 145, 'gi|23268449|gb|AAN11320.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 8.85367e-103, 759, 145, 'gi|297689478|ref|XP_002822173.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 9.0232e-103, 759, 145, 'gi|61679604|pdb|1Y85|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 9.75479e-103, 759, 144, 'gi|58177617|pdb|1YE0|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 9.97238e-103, 758, 144, 'gi|27574248|pdb|1O1O|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.19133e-102, 758, 145, 'gi|29446|emb|CAA23759.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.44901e-102, 757, 144, 'gi|58177625|pdb|1YE2|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.63431e-102, 757, 144, 'gi|61679637|pdb|1Y5F|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.67042e-102, 757, 144, 'gi|2981643|pdb|1A00|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.96749e-102, 757, 145, 'gi|229959|pdb|1HBS|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.42427e-102, 756, 144, 'gi|2982014|pdb|1ABY|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.451e-102, 756, 145, 'gi|442751|pdb|1CMY|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.652e-102, 756, 145, 'gi|13549112|gb|AAK29639.1|AF349114_1');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.88963e-102, 755, 144, 'gi|60594385|pdb|1YIH|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.88963e-102, 755, 144, 'gi|60594302|pdb|1YEN|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.98702e-102, 755, 145, 'gi|3660434|pdb|6HBW|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.05373e-102, 755, 144, 'gi|27574230|pdb|1O1I|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.12191e-102, 755, 144, 'gi|61679728|pdb|1Y2Z|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.26278e-102, 755, 145, 'gi|323463178|pdb|3QJC|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.44767e-102, 755, 145, 'gi|494071|pdb|1HBA|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.55585e-102, 755, 144, 'gi|999565|pdb|2HHE|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.84884e-102, 755, 145, 'gi|3660145|pdb|1BUW|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.97788e-102, 755, 144, 'gi|60594354|pdb|1YGF|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.02183e-102, 754, 144, 'gi|61679764|pdb|1Y4Q|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.02183e-102, 754, 144, 'gi|61679768|pdb|1Y4R|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.06626e-102, 754, 145, 'gi|300508775|pdb|3NL7|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.24883e-102, 754, 144, 'gi|61679772|pdb|1Y4V|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.39101e-102, 754, 144, 'gi|61679645|pdb|1Y5K|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.48838e-102, 754, 144, 'gi|27574235|pdb|1O1K|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.53786e-102, 754, 144, 'gi|61679596|pdb|1Y7Z|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.53786e-102, 754, 144, 'gi|61679657|pdb|1Y7G|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 5.40635e-102, 754, 144, 'gi|58177621|pdb|1YE1|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 5.77254e-102, 753, 146, 'gi|187940241|gb|ACD39349.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 6.16315e-102, 753, 145, 'gi|1942686|pdb|1GBV|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 8.19748e-102, 752, 144, 'gi|61679653|pdb|1Y7D|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 8.6592e-102, 752, 144, 'gi|122616|sp|P02025.1|HBB_HYLLA');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 8.75456e-102, 752, 144, 'gi|2981647|pdb|1A01|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 9.66553e-102, 752, 143, 'gi|5822282|pdb|1QI8|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.03276e-101, 752, 144, 'gi|61679600|pdb|1Y83|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.11566e-101, 752, 144, 'gi|58176647|pdb|1RQA|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.15315e-101, 751, 144, 'gi|223012|prf||0404170B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.23189e-101, 751, 144, 'gi|60594314|pdb|1YEU|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.53438e-101, 751, 144, 'gi|60594341|pdb|1YG5|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.22572e-101, 750, 144, 'gi|40886941|gb|AAR96398.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.16238e-101, 749, 143, 'gi|27574252|pdb|1O1P|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 6.89227e-101, 746, 144, 'gi|1942682|pdb|1GBU|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 7.12197e-101, 746, 142, 'gi|122668|sp|P02032.1|HBB_SEMEN');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.25044e-100, 745, 141, 'gi|122593|sp|P19885.2|HBB_COLPO');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.46649e-100, 741, 141, 'gi|62901561|sp|Q6WN22.3|HBB_ATEPA');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 7.71036e-100, 740, 141, 'gi|62901547|sp|P68232.2|HBB_ATEGE');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 8.51711e-100, 739, 140, 'gi|62901537|sp|P68222.2|HBB_MACFU');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 9.20258e-100, 739, 141, 'gi|62901583|sp|Q6WN27.3|HBB_PITPI');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 9.30485e-100, 739, 141, 'gi|62901562|sp|Q6WN25.3|HBB_LAGLA');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 9.60209e-100, 739, 140, 'gi|122584|sp|P02028.1|HBB_CERAE');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.87936e-99, 737, 142, 'gi|296217282|ref|XP_002754937.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.44135e-99, 736, 139, 'gi|256600242|ref|NP_001157900.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.81769e-99, 736, 140, 'gi|62901529|sp|P67821.3|HBB_CEBAP');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.21723e-99, 736, 140, 'gi|169402677|gb|ACA53486.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.09957e-99, 735, 140, 'gi|62901560|sp|Q6WN21.3|HBB_CALGO');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.03908e-98, 732, 139, 'gi|86611|pir||C24693');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.34122e-98, 731, 139, 'gi|285026390|ref|NP_001162318.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.64976e-98, 731, 139, 'gi|122591|sp|P02033.1|HBB_COLBA');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.76411e-98, 731, 139, 'gi|62901575|sp|P02036.2|HBB_SAISC');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.19303e-98, 730, 141, 'gi|122577|sp|P18985.1|HBB_CALAR');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.31607e-98, 730, 138, 'gi|122636|sp|P08259.1|HBB_MANSP');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.50118e-98, 730, 140, 'gi|62901565|sp|Q6WN29.3|HBB_ALOBE');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.95049e-98, 729, 138, 'gi|297689480|ref|XP_002822175.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.11401e-98, 729, 138, 'gi|122634|sp|P02026.1|HBB_MACMU');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.47458e-98, 729, 137, 'gi|229149|prf||610523A');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 3.67115e-98, 729, 139, 'gi|122682|sp|P02039.1|HBB_SAGFU');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.33186e-98, 728, 139, 'gi|122563|sp|P02035.1|HBB_AOTTR');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.42834e-98, 728, 139, 'gi|122586|sp|P02031.1|HBB_CERTO');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.52694e-98, 728, 139, 'gi|122582|sp|P02040.1|HBB_CEBAL');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 4.94333e-98, 728, 139, 'gi|62901577|sp|P68054.1|HBB_SAGNI');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 5.34545e-98, 728, 139, 'gi|62901563|sp|Q6WN26.3|HBB_AOTAZ');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 6.87256e-98, 727, 137, 'gi|4504351|ref|NP_000510.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 7.82839e-98, 726, 139, 'gi|229304|prf||690953A');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.38638e-97, 725, 138, 'gi|122659|sp|P02030.1|HBB_PAPCY');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.65547e-97, 724, 136, 'gi|18462105|gb|AAL72117.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 1.78515e-97, 724, 138, 'gi|54037251|sp|P67822.1|HBB_CEBCA');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.01375e-97, 724, 138, 'gi|122683|sp|P02038.1|HBB_SAGMY');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_1', '1499', 2.3212e-97, 723, 139, 'gi|229385|prf||711685A');

insert into querysequences values('prot_2', 'MEMFQGLLLLLLLSMGGTWASKEPLRPRCRPINATLAVEKEGCPVCITVNTTICAGYCPTMTRVLQGVLPALPQVVCNYRDVRFESIRLPGCPRGVNPVVSYAVALSCQCALCRRSTTDCGGPKDHPLTCDDPRFQDSSSSKAPPPSLPSPSRLPGPSDTPILPQ');
insert into experiments (id, program, matrix, evalue, maxgaps, dbase) values (37997, 'blastp', 'BLOSUM62', 3.47458e-98, 11, 'nr');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.43056e-115, 847, 165, 'gi|30583985|gb|AAP36241.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.68389e-115, 846, 165, 'gi|4502789|ref|NP_000728.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.69786e-115, 849, 165, 'gi|281185508|sp|Q6NT52.4|CGB2_HUMAN');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 5.94857e-115, 843, 164, 'gi|61364497|gb|AAX42553.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.23861e-114, 840, 164, 'gi|76826792|gb|AAI06724.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.84084e-114, 839, 164, 'gi|26996824|gb|AAH41054.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.6706e-114, 837, 162, 'gi|157840875|gb|ABV83054.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 9.98693e-114, 835, 163, 'gi|157840876|gb|ABV83055.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.96794e-113, 833, 163, 'gi|180444|gb|AAA53287.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 5.3414e-113, 830, 162, 'gi|15451750|ref|NP_149133.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.73038e-112, 823, 161, 'gi|119572820|gb|EAW52435.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 3.93281e-111, 817, 160, 'gi|132566538|ref|NP_203696.2|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 5.86754e-110, 809, 159, 'gi|18448424|gb|AAL69705.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 6.55917e-109, 802, 158, 'gi|18448428|gb|AAL69707.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.30738e-108, 803, 156, 'gi|193806756|sp|A6NKQ9.3|CGB1_HUMAN');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.03122e-108, 799, 157, 'gi|18448426|gb|AAL69706.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 5.33275e-105, 776, 152, 'gi|132566537|ref|NP_203695.2|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.44509e-102, 758, 148, 'gi|133778289|gb|AAI26461.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.71455e-99, 739, 145, 'gi|640446|pdb|1HCN|B');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.77476e-98, 733, 144, 'gi|1335012|emb|CAA25069.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.08447e-92, 695, 159, 'gi|157840877|gb|ABV83056.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 6.31834e-86, 652, 142, 'gi|297705418|ref|XP_002829574.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.18647e-85, 650, 146, 'gi|18448422|gb|AAL69704.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.25945e-85, 650, 141, 'gi|297705432|ref|XP_002829579.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 3.47437e-85, 647, 145, 'gi|18448432|gb|AAL69709.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 5.07198e-85, 646, 140, 'gi|297705430|ref|XP_002829578.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.03896e-84, 642, 140, 'gi|297705426|ref|XP_002829576.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.93909e-84, 640, 140, 'gi|18448438|gb|AAL69712.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.21825e-83, 637, 139, 'gi|297705428|ref|XP_002829577.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 9.81605e-83, 630, 137, 'gi|18448440|gb|AAL69713.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.08032e-82, 626, 137, 'gi|18448434|gb|AAL69710.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.8717e-80, 615, 136, 'gi|18448436|gb|AAL69711.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.61616e-80, 617, 116, 'gi|297705424|ref|XP_002829583.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.48413e-76, 587, 130, 'gi|18448472|gb|AAL69729.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.93624e-74, 574, 141, 'gi|332267625|ref|XP_003282783.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.04423e-73, 570, 116, 'gi|115392101|ref|NP_001065271.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.19856e-73, 571, 141, 'gi|332241095|ref|XP_003269724.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.9822e-73, 570, 128, 'gi|18448468|gb|AAL69727.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.22531e-73, 568, 115, 'gi|90185267|sp|Q2Q1P1.1|LSHB_GORGO');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.65133e-73, 567, 108, 'gi|297705420|ref|XP_002829575.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.53377e-73, 565, 115, 'gi|157840873|gb|ABV83052.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.9759e-73, 567, 128, 'gi|18448466|gb|AAL69726.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 6.5137e-73, 564, 115, 'gi|4504989|ref|NP_000885.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.18166e-72, 563, 126, 'gi|18448462|gb|AAL69724.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.69031e-72, 563, 134, 'gi|13027716|gb|AAK08644.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 3.22396e-72, 560, 107, 'gi|90185269|sp|Q2Q1P0.1|LSHB_PONPY');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 5.7591e-72, 558, 106, 'gi|18448454|gb|AAL69720.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 7.28949e-72, 560, 134, 'gi|297277569|ref|XP_002801382.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.08211e-71, 559, 133, 'gi|162951940|ref|NP_001106126.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.37595e-71, 558, 134, 'gi|13027714|gb|AAK08643.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.20042e-71, 554, 124, 'gi|18448470|gb|AAL69728.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 6.59244e-71, 554, 134, 'gi|74136405|ref|NP_001028100.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 3.0506e-70, 548, 123, 'gi|18448448|gb|AAL69717.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.47236e-70, 547, 122, 'gi|18448442|gb|AAL69714.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.8826e-70, 547, 122, 'gi|18448450|gb|AAL69718.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.22512e-69, 544, 122, 'gi|18448444|gb|AAL69715.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.71832e-69, 542, 103, 'gi|18448452|gb|AAL69719.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 3.39459e-69, 542, 121, 'gi|18448464|gb|AAL69725.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.55788e-69, 541, 121, 'gi|18448474|gb|AAL69730.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.04402e-68, 536, 120, 'gi|18448446|gb|AAL69716.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.24099e-66, 524, 112, 'gi|116243051|sp|Q3HRV3.1|CGHB_AOTNA');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.47279e-65, 518, 109, 'gi|218117109|emb|CAQ52836.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 3.6935e-65, 516, 112, 'gi|296234311|ref|XP_002762382.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.83827e-64, 508, 110, 'gi|218117138|emb|CAQ52834.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.16123e-63, 506, 113, 'gi|218117137|emb|CAQ52833.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.50722e-62, 498, 98, 'gi|18448478|gb|AAL69732.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.50153e-61, 489, 95, 'gi|18448458|gb|AAL69722.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.82442e-61, 489, 104, 'gi|297277565|ref|XP_002801383.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.97013e-61, 491, 107, 'gi|218117134|emb|CAQ52832.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.47167e-61, 489, 110, 'gi|218117133|emb|CAQ52831.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 7.99858e-61, 485, 103, 'gi|62510783|sp|Q6EV78.1|LSHB_MACFA');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.34095e-60, 483, 93, 'gi|18448460|gb|AAL69723.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.44797e-60, 483, 93, 'gi|18448456|gb|AAL69721.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 7.04128e-60, 481, 104, 'gi|218117131|emb|CAQ52830.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.34249e-59, 479, 107, 'gi|116243053|sp|Q3S2X5.1|CGHB_SAIBB');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.06227e-59, 473, 96, 'gi|223127|prf||0511229A');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.86434e-58, 472, 99, 'gi|6016517|sp|O46641.1|LSHB_EQUBU');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.41943e-58, 468, 97, 'gi|18448476|gb|AAL69731.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 5.86756e-57, 459, 86, 'gi|18448488|gb|AAL69737.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 8.51117e-57, 461, 100, 'gi|218117112|emb|CAQ52838.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.42267e-56, 459, 103, 'gi|218117111|emb|CAQ52837.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 3.25711e-56, 455, 91, 'gi|27806855|ref|NP_776355.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 7.31901e-56, 452, 92, 'gi|75065953|sp|Q8WN18.1|LSHB_AILME');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.03387e-55, 454, 97, 'gi|1170833|sp|P19794.2|LSHB_EQUAS');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.18018e-54, 444, 89, 'gi|163301|gb|AAA30623.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.16517e-54, 440, 82, 'gi|18448486|gb|AAL69736.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 9.3584e-54, 438, 81, 'gi|18448482|gb|AAL69734.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.05137e-53, 441, 95, 'gi|308153311|ref|NP_001184022.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 3.03961e-53, 435, 88, 'gi|99029192|gb|ABF60882.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.68762e-53, 434, 80, 'gi|57163809|ref|NP_001009277.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.98911e-53, 433, 80, 'gi|18448484|gb|AAL69735.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 6.04184e-53, 433, 90, 'gi|408241|gb|AAB27819.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 6.53671e-53, 432, 80, 'gi|133711972|gb|ABO36676.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 7.53585e-53, 431, 81, 'gi|133711968|gb|ABO36674.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 1.92534e-52, 430, 89, 'gi|75064995|sp|Q8HZR9.1|LSHB_AILFU');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 2.50927e-52, 429, 88, 'gi|281348374|gb|EFB23958.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 3.12422e-52, 427, 79, 'gi|133711964|gb|ABO36672.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.15221e-52, 427, 79, 'gi|133711966|gb|ABO36673.1|');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.23076e-52, 428, 90, 'gi|126480|sp|P01232.2|LSHB_PIG');
insert into alignments (query, experiment, evalue, score, identity, externalid) values ('prot_2', '37997', 4.78637e-52, 426, 79, 'gi|133711960|gb|ABO36670.1|');

insert into querysequences values('prot_3', 'MVHLTPVEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH');
insert into experiments (id, program, matrix, evalue, maxgaps, dbase) values (3, 'blastp', 'BLOSUM62', 3.47458e-98, 11, 'nr');

insert into experiments (id, program, matrix, evalue, maxgaps, dbase) values (4, 'blastp', 'BLOSUM62', 3.47458e-98, 11, 'nr');

insert into scientists (title, fam_name, initials, experiment) values ('MSc', 'Herber', 'M', 1499);
insert into scientists (title, fam_name, initials, experiment) values ('BSc', 'Wedema', 'R', 1499);
insert into scientists (title, fam_name, initials, experiment) values ('Drs', 'Plomp', 'P', 37997);
insert into scientists (title, fam_name, initials, experiment) values ('Dr', 'Stapel', 'D', 4);

