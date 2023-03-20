MaxHP = 20
HP = MaxHP
print(r"""\                                                                                  
      ,/   .`|                          ,-.----.                                          
    ,`   .'  :   ,---,                  \    /  \                     ___       ,---,     
  ;    ;     / ,--.' |                  |   :    \                  ,--.'|_   ,--.' |     
.'___,/    ,'  |  |  :                  |   |  .\ :                 |  | :,'  |  |  :     
|    :     |   :  :  :                  .   :  |: |                 :  : ' :  :  :  :     
;    |.';  ;   :  |  |,--.    ,---.     |   |   \ :    ,--.--.    .;__,'  /   :  |  |,--. 
`----'  |  |   |  :  '   |   /     \    |   : .   /   /       \   |  |   |    |  :  '   | 
    '   :  ;   |  |   /' :  /    /  |   ;   | |`-'   .--.  .-. |  :__,'| :    |  |   /' : 
    |   |  '   '  :  | | | .    ' / |   |   | ;       \__\/: . .    '  : |__  '  :  | | | 
    '   :  |   |  |  ' | : '   ;   /|   :   ' |       ," .--.; |    |  | '.'| |  |  ' | : 
    ;   |.'    |  :  :_:,' '   |  / |   :   : :      /  /  ,.  |    ;  :    ; |  :  :_:,' 
    '---'      |  | ,'     |   :    |   |   | :     ;  :   .'   \   |  ,   /  |  | ,'     
               `--''        \   \  /    `---'.|     |  ,     .-./    ---`-'   `--''       
                             `----'       `---`      `--`---'                                                                                                         
                   _______________________________________________________                                                
                  |       //    ) )                                       |  
                  |      //             ___        _   __        ___      | 
                  |     //    / /     //___) )   // ) )  ) )   //   ) )   |
                  |    //    / /     //         // / /  / /   //   / /    |  
                  |   //____/ /     ((____     // / /  / /   ((___/ /     |
                  |_______________________________________________________|
                  """)
print("SEI UN VECCHIO SIGNORE UMANO NEI BASSIFONDI DI SOLTERRA, NON POSSIEDI NULLA, HAI PERSO TUTTO. TI TROVI IN UN VICOLO BUIO E, COME OGNI GIORNO, STAI FISSANDO IL VUOTO MA QUESTA VOLTA INTRAVEDI UN'OMBRA UN PO' BIZZARRA E INUMANA:")
input("SATANA: Salve, mortale, non penso ci sia bisogno di presentarmi. Sono qui per un patto, o per meglio dire, un contratto: voglio offrirti l'eterna giovinezza e l'eterna ricchezza in cambio di un favorino, a più tardi le spiegazioni. Allora, ci stai?")
Scelta = input()
if Scelta == "No":
    print("SATANA: Cosa?!?!? Sei un pazzo a rifiutare una richiesta del diavolo in persona! Ti meriti di morire!")
    input("SEI MORTO")
    print("Causa: Ti sei messo contro SATANA e ti ha ucciso")
    input("Vuoi rigiocare?")
    Scelta = input()
    if Scelta == "No":
        quit()
    elif Scelta == "Si":
        print("SATANA: Allora procediamo, firma in fondo il foglio")
Nome = input()
if Nome == "Gesù":
    print("Luca Acampora: Ti credi simpatico? Cambia nome.")
    Nome = input()
    print("sei sicuro?")
CheckNome = input()
if CheckNome == "No":
    print("SATANA: ti sei dimenticato per caso il tuo nome? Muoviti se non vuoi fare una brutta fine")
    Nome = input()
print("SATANA: Ok, ora ti spiego in cosa consiste il contratto.")
input("SATANA: Dovrai ammazzare 6 miei seguaci, si fanno chiamare IUDICES. Mi hanno tradito, stanno attuando una ribellione per abbattermi e tu dovrai fermarli.")
input("SATANA: Ecco: questa è la tua armatura. Sarai simile ad un gladiatore romano, anche se... dovrai indossare questo sacchetto di carta, SEMPRE; una volta ammazzato uno degli IUDICES dovrai raccogliere il sangue col sacchetto e poi indossarlo. Vai tranquillo, questa è solo una prova della tua fiducia.")
input("hai ottenuto: Sacco di Carta (Oggetto chiave)!")
input("hai ottenuto: Armatura (Oggetto chiave)!")      
input("SATANA: e questa sarà la tua arma:")
input("hai ottenuto: Daga")
input("SATANA:La tua prima destinazione sarà Necromorus, lì troverai Euronymous Il Principe della Morte, sarà la tua prima vittima")

input("SONO PASSATE 13 ORE DALLA PARTENZA DA SOLTERRA E COMINCI A INTRAVEDERE IL REGNO DI NECROMORUS")
input("SEI ENTRATO NEL REGNO. LA CITTà è TETRA, OSCURA E GLI EDIFICI RICORDANO UNO STILE BAROCCO MA ANCHE GOTICO, QUESTA CITTà è MOLTO ANGOSCIANTE.")
input("UNA VECCHIA TI BLOCCA, SEMBRA AVERE IN MANO UNA SPECIE DI FOTOCAMERA, VUOI ALLONTANARTI?")
Scelta = input()
if Scelta == "No":
    print("Anziana: Lei! Lei! Ha una oscura presenza che la perseguita... poi...")
    input(" è spacciato...")
    input("LA VECCHIA TI LASCIA UNA FOTO")
    input("hai ottenuto: Foto Angosciante!")
    input("VUOI ISPEZIONARLA?")
    Scelta = input()
    if Scelta == "Si":
        print("VEDI LA FOTO DI UNA PERSONA, MORTA ACCASCIATA A TERRA IN MEZZO AL SANGUE. HA UN SACCHETTO DI CARTA IN TESTA E UN'ARMATURA MOLTO SIMILE ALLA TUA")
print("TI GUARDI IN GIRO E VEDI TRE STRADE:")
input("ANDANDO DRITTO VEDI UN GRANDE PALAZZO MOLTO SOSPETTO, CHISSà MAI COSA CI SARà Lì DENTRO")
input("A DESTRA VEDI UNA PIAZZA, NON SEMBRA PERò RAGGIUNGIBILE")
input("A SINISTRA VEDI UN VIALE CON TANTE DIRAMAZIONI, è LA DIREZIONE NELLA QUALE SI è INCAMMINATA LA VECCHIA DI PRIMA")
input("(Tutorial: scrivi w, a, s, o d per muoverti quando ce n'è la possibilità. Alcune volte delle direzioni non saranno disponibili)")
DirezioniDisponibili = ["w", "d"]
Scelta = input()
if Scelta not in DirezioniDisponibili:
      print("NON PUOI ANDARE IN QUELLA DIREZIONE!")
elif Scelta == "d":
    print("TI AVVII NEL VIALE, AD UN CERTO PUNTO INTRAVEDI UNA PERSONA PIUTTOSTO BASSA E GOBBA PARLARE CON UNA COPPIA DI PERSONE")
    input("NOTI CHE IN QUESTA CITTà TUTTE LE PERSONE SEMBRANO APATICHE, CHISSà PERCHè, FORSE PER LA SCARSA QUANTITà DI LUCE")
    input("PIù TI AVVICINI A QUELLA PERSONA, PIù NOTI CHE ASSOMIGLIA ALLA VECCHIA CON LA FOTOCAMERA")
    input("è PROPRIO LEI, PERò QUEST'ULTIMA TI VEDE E COMINCIA A SCAPPARE")
    input("Anziana: Ancora tu! BESTIA DI SATANA!")
    input("SPUNTANO DELLE GUARDIE DA TUTTE LE PARTI, HANNO ARMATURE DORATE E CON UNO STRANO SIMBOLO SUL PETTO. DENTRO L'ARMATURA NON SEMBRA ESSERCI UN ESSERE VIVENTE")
    input("NON PUOI AFFRONTARLE TUTTE, DEVI SCAPPARE")
    input("RIESCI A SCAPPARE E PER PURA FORTUNA TI RITROVI NEL PUNTO DI INIZIO")
    input ("TI GUARDI IN GIRO E VEDI TRE STRADE:")
    input("ANDANDO DRITTO VEDI UN GRANDE PALAZZO MOLTO SOSPETTO, CHISSà MAI COSA CI SARà Lì DENTRO")
    input("A DESTRA VEDI UNA PIAZZA, NON SEMBRA PERò RAGGIUNGIBILE")
    input("A SINISTRA VEDI UN VIALE CON TANTE DIRAMAZIONI, DOPO QUELLO CHE è SUCCESSO NON PENSO SIA PIù PERCORRIBILE")
    DirezioniDisponibili = ["w"]
    if Scelta not in DirezioniDisponibili:
        print("NON PUOI ANDARE IN QUELLA DIREZIONE!")
    elif Scelta == "w":
        print("C'è UNA GUARDIA, DEVI DIFENDERTI!")
        input("INIZIA LA BATTAGLIA CON GUARDIA DI EURONYMUS!")
        input("(Tutorial: prima di ogni battaglia potrai selezionare le armi per il combattimento, ogni arma infligge il proprio danno, adesso però potrai usare solo la Daga)")
        input("Arma: Daga (5 ATK)")
        input("(Tutorial: durante la battaglia potrai scegliere se usare il tuo turno per: attaccare, agire, inventario o scappare.)")
        input("(Tutorial:  Agendo potrai sviluppare una relazione di amicizia oppure flirtare con l'avversario, dipende dalle tue skill sociali. Con l'inventario potrai curarti o usare oggetti di varia utilità. Da alcune battaglie non si può scappare)")
        print(r"""\
     +-------------------------------------------------------------------------------------------------------------------------------------+
                                                        ____ _   _   _    ____  ____ ___    _    
                                                       / ___| | | | / \  |  _ \|  _ |_ _|  / \   
                                                      | |  _| | | |/ _ \ | |_) | | | | |  / _ \  
                                                      | |_| | |_| / ___ \|  _ <| |_| | | / ___ \ 
                                                       \____|\___/_/   \_|_| \_|____|___/_/   \_\
                                                                                                                                                                                                                           
                                                                                                                                      
                                                                                                                                      
                                                                                                                ..                    
                                                                                                                ':.                   
                                                                                                                .;.                   
                                                                                                                .;.                   
                                                                                                               .;'                    
                                                                                                              .;,                     
                                                                                                             .c;                      
                                                                                                        .  .;o;                       
                                                                    ..,:coddxxkkkxddol:;'..             .,,,oo'                        
                                                               .;lxkOXNWWWWWNNNNNNNNNNXXK0koc,.         .cxdc.    .,.                  
                                                            .cxKNWWWWWWWWWNNNNNNNNNNNNXXXXXXKKOdc,.   .;dko,.     ';.                  
                                                         .;dKWWWWWWWWWWWWNNNNNNNNNNNXXXXXKKKKKK00Od:,cxOd:.      .,.                   
                                                        ;kXWWWWWWWWWWWWNNNNNNNNNNXXXKKKKKXKKKK0OkkkOOko:'.     .',.                    
                                                      'dXWWWWWWWWWWWWNNNNNNNNNNXXKKKKKKKKKK00OkxkOko:'.....  ..'.                      
                                                    .:0WWWWWWWWWWNNNNNNNNXXXNNXXK00KKK0000OOkkkkxl,......',;cc'                        
                                                   .oXWWWWWWWWNNNNNNNNXXXXXNNXK0OO0OOOOOOkkk0Oo:'...'..,coxdc,. .;.                    
                                                  .oNNWWWWWWNNNNNNXXXXXXXNNNXK0OOOOkkkkxxkOOd;.....'',lxxl;'.....c'                    
                                                  cXWWWNNNNNNNNXXXXXXXXNNNNNXKK0OkxxxddxOOo;'....'',lxdc,.....,..:,      .,.           
                                                 'OWWNNNNNNNXXXXXXXXXNNNNNNXXXXKOxddoox0kc,.....',ldo;..........,l'      .c;           
                                                 oNWWNNNNXXXXXXNNXNNNWWNXKXXXNNN0dllllxkool'.'',lxo,...'....',:ldc.      .:'           
                                                '0WWWWNNXXXKXXNNXXNNNNKKKXXNNNNNXkl;;;lxdxd:cloxd;..'.,:cccllcc;...      ';.           
                                               .oWWNWNXXXXKKXWWXXK0kkdodxkO0KKKKKKOc..,ldxddOkdd,..,:;,;;;;,......'.   .;:.            
                                               ;KWWNK0KKK00KNWKko;........',:lodolllc,'cdodkxooxo;;:,.. ..........',,;cc;.             
                                              .kWWNKxoxO000XXOo;.            ..''.';cl;,coddlcoxol;. ....''....';codoc,.               
                                              ,0Kko;..,cdOXNOo:'..                .'ldl,';cllc:cldd:'...,;:ccccccc;...                 
                                             .lxc,......:KWXOdl;,.                 .,xd,..,,;clodkkxo:;;,''',''........                
                                             .c:...... .dWNK0kdc,.              ... .ox, .',;,;lllooll;.   ..   ...','.  ..            
                                              .''..    'd0XK0Okd:.           .......,xd;. ..,..'',,;col.....  .,,,;;......     .       
                                               .,'.   .,,'cxO00Od;.     ...........,xOxd,   ..',;,..;cllc:;;;:c:;;:,.'..    .';,.      
                                                .;.   .c;...ckO0KOo:,....'''''''';oO00O0kc''............',;;;,........     .;;,..      
                                                .;;.. ,x:....,dkO000Okoc::ccccloxkkkkkkkkxdddol;'....................    .,;,','       
                                                 ;o:'.ok;.    ,oxxxdxkkkxxxxxxdolccllcccccclol:...       ....      .   .';;;;,;'       
                                                .oKOxxKd.   ...,odoooooolc::;;;;:ccc:::;;,,'.       ...           ..  .;::;;:::'       
                                                ,0WNK00d. ...'.;xxoolllcccc:;;:;;,'........       ..... ..         ..',;;::,c::c,      
                                                ,0NKo:xO:,;coclkOxxddoc:;,,'.....     ...        .........        ..,,;,;c::'.;:;:'    
                                                 ;O0xod0KXNNNXK0Okkkxddl:,'......    .;,..      ..'......       ..'',;,':,.;,';' .;,   
                                                  .;,'.;0WWNNXK00K0Okkxdlc,......   .;l:'..     .;,''....     ..',,,,,'':,.,::;;:;:ol'.
                                                       .kWWNNNKKKX0OOkxdoc,''...  . .od:,.     ':c;;,...     .';;,',::,,;c,.'cc;',;oo;,
                                                       .xNKKKOkdkkloxococ;,''.'...  ;kdc;.   .;lolc:,...    ';;:;',::;;,;cc:;,:;.';cc,,
                                                        c00K0O0dkkodxoloc:,'''..   .dklc:. .,ldddolc;....  .;::::cloc;;:clc;:clddoodoc;
                                                 ....   ;KNXKKKkkkkkxdocc:,''''.  .dOoccc''ldxxxxddo:'.....;c;,;:cccclldl:::;;;;:dxd:,;
                                              .....     'kXKKKK0OOkxxdollc:clool;:kOdlcloodkdooooool:,...;::c::cclolokkxddolooolloolccl
                                           .',..        'ONXXXKOO0000Okkkkkkkkxxk0kolcloxkxolcclcc:,.. .,:ccc;:coddxkkxodlcododdoooodol
                                        .';,..          'OK000OOOOOOOkkkOOOOkkO0Odlcccoxxd:,,,''''.   .':c:clloddxxxdddxxolddool:;,'...
                                       .::...           .oKO000OOOOOO00OOkOO0K0xocccccc:,..   .....   .;ccc:codddddoollc:;,'...        
                                       ;:...            .d0KXK0OOO00KK0OOO0Okxolc;,'...      .''.......':clllolc:;,'...                
                                      .,'....           :0XNXK0OOOkkkxxdolc:;,'...... ...    .;;'.........'''..                        
                                       ''.'.           .oXXXXOxdoolcc:;'....... ..............:c,..'..........                         
                                       .'....           .d0Od:,,,'....       ....,,''...'''. .ld;';,.;..,......                        
                                        .....     ..     .'..                ...,::;,,,,,,'..'dx:;:';:.;:',,',.                        
                                         .....     ...                       .;;;cl:;;;:;,,,..dkll:,l;.lc,c;,c.   ..            .. ... 
                                           ...      ...                      .:cclocccc::::,.,xkdo;cd',xc:o,;o'    ..           .......
                                            ....      .                      'llcodolcllccc:,,xOxl;dl.ck:lo'cd'    ..       ...........
                                                .... ...                     .locoxdlcccloc;':k0x:lx,.dxcx:.oo'.    .'..,,,,'...'......
                                                   ......                    .cdloxkoloolc:clx00xlxo'cklod.'dl,'.';:c:;,'...  .........
                                              .....  ..                       'xOdxOxolllddolo0Kxxxc:xxlxc.:dlclc:;,..      ........  .
                                           ...................                 ,xkxOkdodddoo:cOKkxl,lkodxcclc:,'..     ..  .   .......,
                                        .....................  ......          .lkxkOdodddolco00xl,,oxool:,'..     .........     .';cll
                                     ...................   ..  .........    ....;kkxOkddoool:oKOoclol:;'..    ....';;,,,'''....,:lol:,'
                                    .,'.....................................    .:xxkOdodol:cxOxoc;'..    ...,,,,;lc,;:;,',;:lolc;'.   
                                   ....................................          .cddOxllllddo:,...   ..'';cccc:lolc:cccllol:;'..     .
                                  ...............................                 .clxxoodl;'.  .....'';coclooocooccodolc;'.. .........
                                  .'''.....................'''..                  .:oddc;.........,::cooolclllddooolc;'..  ....,,;:ccll
                                    ....................';;,'.                 .':oo:,........'',;:cclodooddolooc;,...  ...';c:coddxdod
                                         ........  ....'cc;'.                .;ll:,.. .....,;;;:lodlcdxdolool:;'........,cc:ooodxddxxkk
                                     ...';,'.'..'.  ...:o:,..             .,cc;'.  ....',;::loooocclooddoc:;.......',coccdxxxxkkkkxxOOk
                                  .'cccll:;;;,,:;.    .co:;. .         .';c;... ...',;:clooololcc;:odol;'.......;ccldkxookxoxkkkddddxxx
                              ..,:oxdoooooool,cc.   . .cl;''.........,;lllc......'::cooddooollllolloc,'.....,:;;cllloxkOkxxdxOOOxxkxkkO
                            .;dxkO0OOkkxxkoc::l'   .. .:dc;:c::;;;cllcc:;,'...';::lldxxddddolcodl:,..;:,;;;;:cccoodxkOkOOxkOOkxkKK0kkkx
                          .:xOOO0000O00kdxdl:l:.  ..  .':odlld:',,,,'.......,;,,coxxddllddodol:'...,od;.',c::clldkkOxdkOOkxkOkxOO0kk0O0
                        ':dO00O0000O00kolloool..  .. ..'.co,,;....  ..''..'',:cccclcoddddoc;'.',;:lkOl:c''c:;locdOkxxxkddkxO0OkkkkkOOkk
                     .,okO0O00O00000OOdoooc:;..   .. ...;l'':......''',,''',;cc:clllodl:;...;cclllxOxccd;.coccodxxxxkkdddxkkxxdoolllc::
                    .lkOOOOOO00OOOkkkkd:'.        '. ..,l:;c,....'....',,';clll:cllc:,.  .:lllodxxkkkxoc, .lxddxxxxxddollcc:;,'........
                  'lxOOOOOOO0000OOkko;......      ,'...;:';;....,,...',,;:;;:clooc;.   'cllcdkxxkOkkko:'.   'ccllc:;;,.................
                 .;oddxkO0KKKK0K0kl,..'';..       ,,...;:,,...''''...'',;:::lll:,.   .clcloollodkdxOd:,.              .............. ..
                       ..':c:;;;;;;.'c;:;.        ',....'...,,,,''..';;,;llcc:'.   'clcoxkxkOkdodokkc:.           ...................',
                         .,;....'lx;cl;l'         .'...''..',,'''...';;:cll:'.   ,llclxkxxOOkOOxodkol;           ..... .....''.....',cc
                          ..;;'.:kk;ol;o'          ....'...'..',''',,;;cc:'.  .,llcldkkxxkOxlxOolkxoc.          . ..'..''..','.',',;:,'
                          .;c:''oxd:od,oc.         ....'. .,,',;',,;,,,'..  .;lllloddkOkdoooodx;lkoo:          .. ..,,...':;...';:c;';;
                        .::col'ckxklckc,oo:.. .'......'.  .;;,'.....      .:lccldxdlloxkxxdcldo;ldlo,       .........'..,:,.'.'cc;,'..'
                       'oo,.;ccxOOOkolxdccodolo:... .'.    ..         .':clllokkdkOOxoodloxooollxoco.        ..  .....,;,....;c;,,,,,''
                      ,lc'.   ,kkkkxOl;ldl;;dOl... ....         ..',:llccccloddxkkOOOOkxdodxxdc;occl.        .. ..........';:;;;c::c:cl
                     .;'.     ;xkxooxllolcok0x'.    ..   ...',:ccccccllcodxdxkkkOOkkkdooxxxdolcco:;l.        .. .....'''..'',;clcclccll
                             .lxxdodolodccx0O:..        .,,;:;;;,';::cxddkkkdccxOkkkxxxkooxl:cccc,'c'        .........';clolccllolllc:;
                             ,xxol:clooc;cx0d'.        .::'..';l:,:lcll:o0Olc;,o0Okxddxddkkd:'.,;'.;,         ......''';::codolc:;,... 
                            .lo:::cllcc:;:xO;..       .lo::;;ccl:;coclc',ckkdxdlxkdoldkOxc,...';;...'.         ......',;;;;,..       . 
                            cd;coddocc::cd0o...  ....,oo;,;'..';';c,:c:,;,,:okxoOOooxxo;.. .,;........          ...'''...              
                           .dx:cdkdc;c:codx;... ....;do,',',,,,''c:':c:ccc:c:cxXXOkd;.  .  .;'.''......      .......             ..... 
                           .ckc'ldoccl;c::c...    .,ol'....'',;'';;,:::ol:;clodl::,.........;,... .....       .                ........
                            ;Ox,cd:ldl:l;:;...    'lc.......','''',;:::c;';odo:...  ...  .''.....  .. ..                      .........
                            ,xOoll;clcll;;'.. .  ':'........',',',cc:;'':odo:,,.,,  .....''.......      ..                     ........
                           .lxdllccc:ccll,...   .:'..,;....''',,',;';:;cccol:,'',... .. ...........      .....                 ........
                          .,locol;l::o:cl'..   .;;...;;....'.,,.,;'..;:;:lc,..';'.... . ...........  .      ..  ..             ........

     |------------------------------------------------------------------------------------------------------------------------------------|
     |------------------------------------------------------------------------------------------------------------------------------------|
     |
     |   +-----------------------------------------------------------------+
     |   |       _  _____ _____  _    ____ ____    _                       |
     |   |      / \|_   _|_   _|/ \  / ___/ ___|  / \                      |
     |   |     / _ \ | |   | | / _ \| |  | |     / _ \                     |
     |   |    / ___ \| |   | |/ ___ | |__| |___ / ___ \                    |
     |   |   /_/   \_|_|   |_/_/   \_\____\____/_/   \_\                   |
     |   |                                                                 |
     |   +-----------------------------------------------------------------+
     |
     |
     |   +-----------------------------------------------------------------+
     |   |       _    ____ ___ ____   ____ ___ 
     |   |      / \  / ___|_ _/ ___| / ___|_ _|
     |   |     / _ \| |  _ | |\___ \| |    | | 
     |   |    / ___ | |_| || | ___) | |___ | | 
     |   |   /_/   \_\____|___|____/ \____|___| 
     |   |
     |   +-----------------------------------------------------------------+
     |
     |
     |   +-----------------------------------------------------------------+
     |   |    ___ _   ___     _______ _   _ _____  _    ____  ___ ___  
     |   |   |_ _| \ | \ \   / | ____| \ | |_   _|/ \  |  _ \|_ _/ _ \ 
     |   |    | ||  \| |\ \ / /|  _| |  \| | | | / _ \ | |_) || | | | |
     |   |    | || |\  | \ V / | |___| |\  | | |/ ___ \|  _ < | | |_| |
     |   |   |___|_| \_|  \_/  |_____|_| \_| |_/_/   \_|_| \_|___\___/ 
     |   |
     |   +-----------------------------------------------------------------+
     |
     |
     |   +-----------------------------------------------------------------+
     |   |    ____   ____    _    ____  ____   _    
     |   |   / ___| / ___|  / \  |  _ \|  _ \ / \   
     |   |   \___ \| |     / _ \ | |_) | |_) / _ \  
     |   |    ___) | |___ / ___ \|  __/|  __/ ___ \ 
     |   |   |____/ \____/_/   \_|_|   |_| /_/   \_\
     |   |                            
     |   +-----------------------------------------------------------------+
     |
     |------------------------------------------------------------------------------------------------------------------------------------|
     |------------------------------------------------------------------------------------------------------------------------------------|
     """)

        HPnemico = 10
        NomeNemico = Guardia
        DannoNemicoMAX = 3
        DannoNemicoMIN = 0
        ATKpersonaggio = 5
        AzioniBattaglia = ["ATTACCA", "AGISCI", "INVENTARIO", "SCAPPA"]
        Azione = input()
        if Azione not in AzioniBattaglia:
            print("COSA STAI FACENDO?")
        elif Azione == "Scappa":
            print("Luca Acampora: provi a scappare? Sei una pussy, questo è il tutorial, non puoi scappare")
        elif Azione == "Inventario":
            print ("Hai:                                   INDIETRO")
            Scelta = input()
            if Scelta == "Indietro":
                #torna indietro
        elif Azione == "Agisci":
            print ("PARLA              INDIETRO")
            Scelta = input()
            if Scelta == "Indietro":
                #torna indietro
            elif Scelta == "PARLA":
                print("Guardia:.....")
        elif Azione == "Attacca":
            HPnemico = HPnemico-ATKpersonaggio
            print("Punti Vita dell'avversario: {HPnemico}")
        input("è IL TURNO DEL TUO NEMICO!")
        DannoNemico = int(random.randint(DannoNemicoMAX, DannoNemicoMIN))
        HP -= DannoNemico
        if DannoNemico < 1:
            print("HAI SCHIVATO IL COLPO, BELLA MOSSA!")
        elif DannoNemico = DannoNemicoMAX:
            print("COLPO CRITICO!")
        input("HAI SUBITO", DannoNemico, "HP")
        input("è IL TUO TURNO!")
        Azione = input()
        if Azione not in AzioniBattaglia:
            print("COSA STAI FACENDO?")
        elif Azione == "Scappa":
            print("Luca Acampora: provi a scappare? Sei una pussy, questo è il tutorial, non puoi scappare")
        elif Azione == "Inventario":
            print ("Hai:                                   INDIETRO")
            Scelta = input()
            if Scelta == "Indietro":
                #torna indietro
        elif Azione == "Agisci":
            print ("PARLA              INDIETRO")
            Scelta = input()
            if Scelta == "Indietro":
                #torna indietro
            elif Scelta == "PARLA":
                print("Guardia:.....")
        elif Azione == "Attacca":
            HPnemico = HPnemico-ATKpersonaggio
            print("Punti Vita dell'avversario: {HPnemico}")
            if HPnemico < 1:
                print("HAI VINTO LA BATTAGLIA!)
                input("hai guadagnato: x5 Pozioni (oggetto)!")
                input("hai guadagnato: Spada Arruginita (arma)!")
                input("hai guadagnato: x1 Soffio Dell'Inferno (incantesimo)!")
                input("ARRIVI DAVANTI AL PALAZZO:")
                print("VEDI UN PORTONE GIGANTE CON UN SIMBOLO STRANO SOPRA: UNA STRANA BESTIA RINCHIUSA IN UN CERCHIO CON UN PENTACOLO CHE FA DA SFONDO")
                input("VUOI ENTRARE?")
                Scelta = input()        
                if Scelta == "No":  
                print("VUOI TORNARE INDIETRO?")
                Scelta = input()
                    if Scelta == "Si":
                    elif Scelta != "No" or != "Si":
        
                    elif Scelta == "No":
                    print("VEDI UN PORTONE GIGANTE CON UN SIMBOLO STRANO SOPRA: UNA STRANA BESTIA RINCHIUSA IN UN CERCHIO CON UN PENTACOLO CHE FA DA SFONDO")
                    input("VUOI ENTRARE?")
                elif Scelta == "Si":
                    print("SEI SICURO?")
                CheckScelta = input()
                if CheckScelta == "Si":
                    print("VEDI UNO STRANO ESSERE, è UN UMANOIDE, SEMBRA UN NON MORTO: HA UN'ARMATURA DA SPARTANO, TRE BRACCIA PER LATO E TRE TESTE; QUEST'ULTIME SONO DEI TESCHI, NON HANNO CARNE. AL COLLO PORTA UNA COLLANA CON LO STESSO SIMBOLO INCISO SULLA PORTA")
                    input("INIZIA LA BATTAGLIA CON EURONYMUS, IL PRINCIPE DELLA MORTE")
                    print(r"""\
     +-------------------------------------------------------------------------------------------------------------------------------------+
                                                       _____                                                
                                                      |  ___|                                               
                                                      | |__ _   _ _ __ ___  _ __  _   _ _ __ ___  _   _ ___ 
                                                      |  __| | | | '__/ _ \| '_ \| | | | '_ ` _ \| | | / __|
                                                      | |__| |_| | | | (_) | | | | |_| | | | | | | |_| \__ \
                                                      \____/\__,_|_|  \___/|_| |_|\__, |_| |_| |_|\__,_|___/
                                                                                   __/ |                    
                                                                                  |___/                     
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNXNWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxdxOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOoc:coONWWMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMWNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0old:..:lkNWMMMMMMMMMMMMMMMMMMMMMMWXKNMMMW0xXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMW0l,cl'.;cxXMMMMMMMMMMMMMMMMMMMMMMMWOd0WNX0xdKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNkc;col::cdXMMMMMMMMMMMMMMMMMMMMMMMMKddko:lodXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKocodollcdXMMMMMMMMMMMMMMMMMMMMMMMMNkl:;:oldXWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMWXOl::clcoKMMMMMMMMMMMMMMMMMMMMMMMMW0olcldllkXWWWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl,;:lclOWMMMMMMMMMMMMMMMMMMMMMMMNkolcll:clokxdodONWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKkkOKNWMWMNXNMMMMMMMMMMMMMMMMWW0l:clccOWMMMMMMMMMMMMMMMMMMMMMMMNkolclcccllcldOXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMWKkocoxOKNXdlOWMMMMMMMMMMMMMMMWXxcccc:cOWMMMMMMMMMMMMMMMMMMMMMMMMKdcclcclccoONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMWNNWWMMMMMMMMWKxooolodl;:OMMMMMMMMMMMMMMMW0occcc:;lKMMMMMMMMMMMMMMMMMMMMMMMMMKdlllc::;oXWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMWXOOkxxOKNWMMMWWNOxdocc::cc:xWMMMMMMMMMMMMMNOolc:;::;dNMMMMMMMMMMMMMMMMMMMMMMMMMKocll::;lKMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMN0dc;;;;:clokKNXOkxdollllc:lclKMMMMMMMMMWNNXkllc:;;:,,kWMMMMMMMMMMMMMMMMMMMMMMMMW0occccclOWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMW0oc'    .';;cldxkxddollllolllcdXMWWMMMWNX0KKo:::::;,'lXMMMMMMMMMMMMMMMMMMMMMMWWWXxolccccdNWMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMWOl;.     ,ccclllloodddoollool::dKWWWWWK0KK0xo:;cl:'';xNWMWWWWWWMWWMMMMMMMMMMMMWXxdlcclcl0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMWN0dl,  ....',,:ccc::x00Oxocllolc::lONNNKxodo:::cloc,,clldxkkkkkx0NNNWWMMMMMMMWWWKxoolcllcxNMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMWX0dlol'.,;;::;;;;::cccdXWWWKkoccool:::oooooolcclool:;;:coolcooooo;;xK0KXNWMMMMMWNOdooc:loloKMMWWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMWNK0X0o:oOOkxdc:;,;clollkNMWMWXdllolc::dkolodl;:cll::cllccoldKKOOd:;cxKXK0NMWWMWKkdool::lllkWWXNNkdKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMXxOWMMMWWKdc:;:looookNMMMW0ooool::dKKkooocclcclc:::,,:lcokkkc';::dkdcokkKKkddooc;:clcdXMXdkKxo0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMWNNMMMMWMW0o:;cllooooONMMMXdllloc;'cOK0xlood0KOOOo:,..,lc;,'.  .,;:;',;;:cll:;,,:cc::OWWKocloodXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMWMMMMWMNxc:clooooooONMMNklll:'',;:ok0xclONXKXXOo;..,loc:,',;:ll:;;,;:lkx,..;clcc:oXWWWkclooo0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMW0occloooooodONMW0oc:. .',;;:lc;cOXXXXKxc;':oc::;;:xKX00d:,';odo:,;:c::c:;dNWN0occlclKMMMMMMMMMMMMMMMMMMMMMWWMMMWXXWMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMNxllcloooloooOWWWOl:cl,''.',;;,;dkkkxo:cc,;c:;,;,,o0XXXx;'',;;',;,;;;,.':k0kocc;..,c0WMMMMMMMMMMMMMMMMMMMWKOXWNOdOWMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMWOlllllollloookKNNO:ckkkxxkxxl;..',;;:ll;,;;;;;;:;,:oxo;''..'...';c;...'cc::cc,. .,lOWWMMMMMMMMMMMMMMMMMWXxoO0olOWMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMKdllcccllc:lc:coxkl',;:cclll:;,;;,;;::ldooxxcclc:;'.....',,,,clodl'..'::::;,'. .:d0NMMMMMMMMMMMMMMMMMMWNOollccOWWNNMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWkclc::lc:;;cc::cll:,.'',:::cc:;'',;oxKWXXWWKKN0d:;,....':::ll:;,.  .;;,'... .lKWMMMMMMMMMMMMMMMMMMMWWNOdoc;;lxxdOXMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0lclc;;:c:;;:lccllcc:'.  ..,...,;lkXKkxl:;;;cloOOd:'. ...,'''''.  ..'..    'kWWMMMMMMMMMMMMMMMMMMMWWKkdooc'';lxKWMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0oll:'.;::;,clllclll:'.',','.,:l00l,.         .;dd;.             ...    .cKWMMMMMMMMMMMMMMMMMMMWWXOolccc;'.,lO0KNMMMMMM
       MMMMMMMMMMWXKNMMMMMMMMMMMMMMMMMWKdlc;..',,',:lllllll:,::''':;:Ox'              .:c.........           ,kNWMMWMMMMMMMMMMMMMMMWWKkoccc::cc:::;cdOXWMMMMM
       MMMMWMMMMMNOxONMMMMMMMMMMMMMMMMMWXkl;'..... .,:cllllc::;,',c,co.   .....''..     ...,:clll:'.     .;lx0NMWMMMWWWMMMMMMMMWWNKOdlcccc;;';llllloxkk0XMMMM
       MMMMWMMMMMWXkxkKWWWMMMMMMMMMMMMMWWWXkc.       .';clllc:::;::','  .,clc;,;;;,.    ...';:c:;,'....;okOkolONWWMMNK0KXXKKK00Okdoccc:;,,,,',cldk0KKKKXNMMWM
       MMWKOkkkOOkxddookXWWMMWMMMMMMMMMMMWWWW0o'.      ..,cllc;,,cc...  ....;cc::::,.  .ol''',;;;::clodxdddoc,;dOOdc;,:oxddddooollc:::;,;::lxOKNWMMMMMMMMMMMM
       WMWNKOkxxolllodoodkKWWWMMMMMMMMWWMWWMMMWXx:.       .,:c:;;:l,.:;.     .,:c;,.  'd0o::::cclollooodooolc;':c:,',codddodoollcclc::;;cdOXWWWMMMMMMMMMMMMMM
       MMMMWNXKOoccclooc:coxkO0KXNNNNNWWMWWMWXKOkxo:;,....'coolccc'.':kx:.     ..',,:dKKkccloolc:;:;;:cllll:,::;:cclooooolllllcllllc::cx0NMMWMMMMMMMMMMMMMMMM
       MMMMWKkxdolccolc;;::cllloddxxxkkO0XX0kxdddddxxdolcloddlccll:;::ck0OxooooxxkOXNKOd:::cllll'     ...,,;;::clllllllollllllllll:;:xKWMMMMMMMMMMMMMMMMMMMMM
       MMMMMWWWNKdcodlccclcc:::ccllooddddoloodddddddolc::loolcccc;:c:::coO00XKKXKkxkkl;;:c::;;;'.     .';::c:,;llllllllllllll:;::cco0WMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMN0dllolc:;,,;cccc:ccllllllollcccccclllcllcloodl:;;:::cccc::cc:::::;'....,ccccloll:,..   .clc:::;:llllcc:;;clcc::coxOXWWWMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMWN0xddxO0000Odl:;:cllllllllccccccc::ccllddoooooc:;';:,,:llllc;'....   .'cl:',cooddxxdl:.  .',';;''''......';;o0KXWMMMWWWMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMWXkkOKNWWWWMMMWWKxl:;;ccc:::::::ccc:;clodocloolc::::c,.;llollllc;:c::::cll;...;oddddxdlc;'';,',;.      .   .. .ckXWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMWKKNWMMMMMWMMMWMMMW0xl::;;;,,,,,;;;,;loddc:llc:cc:;;;c,'lollccclcllc:::::,...'';clodc:;;:cloo:,'..'.    ....... .,lx0NMWMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMWNK0Okxoc;:oxkxooooooc:c:::cc:;..;' .;:::clc::::;::;,....,;,,,;:::cloodooool;:o:.   ...'',,,,''';ldk0XWWMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMWWNNKOdoodooolc:;;:::;..,;''';cc:,'.',''',;;::;..';:;;;:clolloodddxddlll:.     ....';:c::ccccldKWMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMW0doooolllolc:'..... .;;.':l;...';:;:c:;;,,,:,..';;,',clllllllcllloccoolclolollllccc:,',;::::oXMWMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWNKkdoodolc:ccc:,.       ':;;;'..';cc;.':lccc:;,,..;;....;:::ccllc:,,;::c::clodxk0NMWWNKOd:;::c:;dNMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMWWNX0kdlcoddolc:;::;,.. .:l,..;;;:,..'::;,''',,;:cc:,';;,..   ....,;::ccc::::;;:lodkOOKWMMMMMMW0o:c:::,oXMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMWNK00Oxolcllldddocc;''... .:ONWNklcccl;'',,',:c:cc:::;:c'.;:'.         ...';lolccllookNMMMMMMMMMMMMKl:cloc,:0MMWWMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMWWMMWWXOxxdddoollllloollcc;'..';ckNWMWWW0olol:,,,;:::;;::cllccc,.';.';.        ..,:lolloolldKWMMMMMMMMMMMMNd:ckx:;c0MMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMWWWN0xddollc:;,,;lollloccccl0NWWMMWWWMWKolllc:cc;..,:clcc::;;:;,,.'ON0:       ';:cxOdlodkxd0WMMMMMMMMMMMWW0ll0K0klxNMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMWN0xdddl;....  ..:ll;''..,:lkXWWWMMWWMMNxlllc:;:;',c:,,:clc::c;...lNMW0,        .;xOdd0NWWXNWMMMMMMMMMMMMMNOONWMN00WMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMWWWNKkoodo:'.    .,:cc:'.  .;:ccld0NWMWWMMMW0olollcc:,,:cll::lc:;:'. .kWWMWx.        .;d0XWWMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMWNXXXK0kddool,.'ldkxdxkdc;..,oxO0KX0xookXWMMMMMMXdlllll:;l:;:;cd:;;,...  'OWWMMWk,.      .'oXWMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMWX0kxolodddol;.'OWMMMWNOoc;:dXWWMMWMWNXKXWMMMMMMWXdclcclcll;;c::oc;:;'....'OMWMMMWNOo;.    .'cdkOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMWNKOoclddxxol::OWWWWMWKdc:xNMWWMMMMMMWMMMMMMMWWWKoclllloOOxl;,,:l::c:,''...:KMMMMMMMMN0o'   .,;;;;cd0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMWXxoodllddllx0XWMWMMMWWOddlxNMWMMMMMMMMMMMMMMMWXkocllcloxXN0kxxddoc;:c:;,''..:OWMMMMMMMWWk'  .;::::;,;cONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMWWKkxONNOddc'oXWMWMMMMMWWNNNOxKMMMMMMMMMMMMMMMMMMOcclllcclON0lcoloxxl:::;,;;;:;'cXMMMMMMMMMW0l,,cc:cokOkooxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMWNNNWWKxok0OXMMWWMMMMMMMMMMWNWMMMMMMMMMMMMMMMMWKxolllllcl0N0lcclodoc:::;,;,'''.cXMMMMMMMMMMWWXOdccl0WWMWXXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMWKOONMWWMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdoolllllccokkkxxxxoc::;;;,....'.:0WMMMMMMMMMMMWWNOlckWWWMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdlooll::;;;;::c:ccccc:;;;,,.......':kNWWMMMMMMWMMMWW0dONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xollllllc::,..';:::::;;;,,,'.......''',ckXWWWWWMWWMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0xolllllllllc::,...,;;;;,,'....  ....;cccc::lkXWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkoolllllclllllc:;'.  ........     ..;loolllllc:lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWN0dlllllllllllllccc:;,.             .;lllloolllllccclONWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkolllllllcllllcc::;;;;,.           .:llllloollclllcc::dKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0dolllllllccllllc:;;;,,''..         .;ccllllllllllllcc:::l0WMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMWNOdoollllllllllll:;,,;,'''...  ..    .';;:ccllllllllclccc;;;l0WMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkooolllllllllllc:,,,,,''''...'oOOd;...';;;cccllllcccclcc:;;;;c0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkooollllllllccc:;,,,;,''''...,dNWWNK:..';;,;:cllllccccccc:,;::;oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNxoollllcclllll:;,'',,,'''''...';:;,,'....,;;,;:ccccccccccl:,,::::kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkolllolcccllcc:,,,,,,''',,'...'.      ....';:;,;:ccccccclcc:,,;::;cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKooollc;;:clc:;,,;;,,,',,,'''''..       ....,;:;,;:ccccclllc:;,,,;;;xWMMWMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKollc:,'';:c:;;,;;;,,''.........         ....';;;,;:ccclcllc:;,,',,';lood0WMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXdllcc;',;;;,;,,,,,'..                        .;:;,,;::cccllc;,'.',,'.   'xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMXxlollc:;;;:;,,,,'..                           .';;;;,,;;:cll:;;;,;,'.    .'lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0ollllllc:;:;,,....                              ..''''',,;:cccccclc,'.    ..':cclldkkxddk0XNWMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0xoollollllc:;,;,. ..                                 .....',;;ccclcccc:.              .     .,cdkOKWMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMWWWNXKOxoc;..  .;lllllc:;,;;'...                 ...',;ccclol,.   .......,;:ccllccc,              ..,;coxk0KXNWWMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMWMN0o;'..        .,::;,''',,..          ..';:loxO0KXNNWMMMWMWNKk,  ......';:ccclll,.        ..;cok0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMWXXK0xl;'...  .;;,''''..   ...,:codk0KNWMMMMMMMMMMMMMMMMMWWWKd:'. ....,,,;::;..   ..,:ox0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXK0k:. ....';;:lodk0KXNWMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMWXOdc,. ...''....;lxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMWXkccoxOKNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMW0;    .;ldkKWMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0koldOXWMMWMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM


     |---------------------------------------------------------------------------------------------------------------------------------------------------------|
     |---------------------------------------------------------------------------------------------------------------------------------------------------------|
     |
     |   +-----------------------------------------------------------------+
     |   |       _  _____ _____  _    ____ ____    _                       |
     |   |      / \|_   _|_   _|/ \  / ___/ ___|  / \                      |
     |   |     / _ \ | |   | | / _ \| |  | |     / _ \                     |
     |   |    / ___ \| |   | |/ ___ | |__| |___ / ___ \                    |
     |   |   /_/   \_|_|   |_/_/   \_\____\____/_/   \_\                   |
     |   |                                                                 |
     |   +-----------------------------------------------------------------+
     |
     |
     |   +-----------------------------------------------------------------+
     |   |       _    ____ ___ ____   ____ ___ 
     |   |      / \  / ___|_ _/ ___| / ___|_ _|
     |   |     / _ \| |  _ | |\___ \| |    | | 
     |   |    / ___ | |_| || | ___) | |___ | | 
     |   |   /_/   \_\____|___|____/ \____|___| 
     |   |
     |   +-----------------------------------------------------------------+
     |
     |
     |   +-----------------------------------------------------------------+
     |   |    ___ _   ___     _______ _   _ _____  _    ____  ___ ___  
     |   |   |_ _| \ | \ \   / | ____| \ | |_   _|/ \  |  _ \|_ _/ _ \ 
     |   |    | ||  \| |\ \ / /|  _| |  \| | | | / _ \ | |_) || | | | |
     |   |    | || |\  | \ V / | |___| |\  | | |/ ___ \|  _ < | | |_| |
     |   |   |___|_| \_|  \_/  |_____|_| \_| |_/_/   \_|_| \_|___\___/ 
     |   |
     |   +-----------------------------------------------------------------+
     |
     |
     |   +-----------------------------------------------------------------+
     |   |    ____   ____    _    ____  ____   _    
     |   |   / ___| / ___|  / \  |  _ \|  _ \ / \   
     |   |   \___ \| |     / _ \ | |_) | |_) / _ \  
     |   |    ___) | |___ / ___ \|  __/|  __/ ___ \ 
     |   |   |____/ \____/_/   \_|_|   |_| /_/   \_\
     |   |                            
     |   +-----------------------------------------------------------------+
     |
     |-----------------------------------------------------------------------------------------------------------------------------------------------------|
     |-----------------------------------------------------------------------------------------------------------------------------------------------------|
     """)
                    input("Euronymus: TU! Sei stato inviato da SATANA non è vero?!")
                    Inventario = ["Pozione", "Soffio Dell'Inferno"]
                    Soffio Dell Inferno = 1
                    Pozione = 5
                    HpNemico = 50
                    NomeNemico = Euronymus
                    DannoNemicoMAX = 9
                    DannoNemicoMIN = 0
                    ATKpersonaggioMIN = 0
                    ATKPersonaggioMAX = 10
                    AtkArmaPersonaggio = 5
                    DannoPersonaggio = 
                    EffettoFuocoArma = 3
                    Turni = 0
                    AzioniBattaglia = ["ATTACCA", "AGISCI", "INVENTARIO", "SCAPPA"]
                    Turni = 1
                    Azione = input()
                    if Azione not in AzioniBattaglia:
                        print("COSA STAI FACENDO?")
                    elif Azione == "Scappa":
                        print("NON PUOI SCAPPARE DA QUESTA BATTAGLIA")
                    elif Azione == "Inventario":
                        print(" Hai: 5x Pozione, 1x Soffio Dell'Inferno            INDIETRO)
                        Scelta = input()
                        if Scelta == "Pozione":
                              if Hp == MaxHP:
                                print("HAI GIà GLI HP AL MASSIMO")
                              elif Hp < MaxHp:
                                  Hp = Hp + 5
                                  if Hp !> MaxHp:
                                      print("HAI RECUPERATO 5 HP!")
                                  elif Hp > MaxHp:
                                       Hp = MaxHP-HP+5
                                       print("HAI GUADAGANATO", HP)
                                       HP=MaxHP
                        elif Scelta == "Soffio Dell'Inferno":
                            print("LA TUA ARMA HA PRESO FUOCO!")
                            EffettoFuocoArma = 3
                    elif Azione == "AGISCI":
                        print("Euronymus: Zitto! Bestia di SATANA!")
                    elif Azione == "Attacca":
                        DannoPersonaggio = int(random.randint(DannoPersonaggioMAX, DannoPersonaggioMIN))
                            if DannoPersonaggio < 1:
                                print("L'AVVERSARIO HA SCHIVATO L'ATTACCO!")
                            elif DannoPersonaggio = DannoPersonaggioMAX:
                                print("COLPO CRITICO!")
                                input("Euronymus: INFAME! ME LA PAGHI")
                        print("Euronymus ha perso", DannoPersonaggio "HP!")
                        input("è IL TURNO DEL TUO AVVERSARIO!")
                        Turni = 1
                                
