'''
coincidenceIndex: Συνάρτηση που υπολογίζει τον δείκτη σύμπτωσης σε ένα δοσμένο κείμενο ή πίνακα
'''
def coincidenceIndex(Text):
    length = len(Text)
    result=0
    freq = [0]*26 #Πίνακας συχνοτήτων
    for i in Text:
        freq[ord(i)-ord('A')]=freq[ord(i)-ord('A')]+1
    for i in freq:
        result = result + (i*(i-1))/(length*(length-1)) #υπολογισμός πιθανότητας
    return result

'''
vigener: Συνάρτηση που παίρνει σαν είσοδο ένα κρυπτοκείμενο που προέκυψε με
         Vigener cipher και βγάζει 10 διαφορετικές εκδοχές για το αρχικό κείμενο
         και το κλειδί
'''
def vigenere(Text):
    counter = 1
    ltext=coincidenceIndex(Text) #Coincidence Index of original text
    charText=[x for x in Text]
    meanIndexes = [] #Πίνακας που θα αποθηκευτούν οι μέσοι όροι των CI για διαφορετικό μήκος κλειδιού
    possibleKeyLength= round((0.065-0.038)/(ltext-0.038)) #Εύρεση πιθανού μήκους κλειδιού με χρήση του τύπου
    for i in range(2,possibleKeyLength*2): #Επειδή ο τύπος είναι πιθανοτικός ψάχνω σε μια περιοχή γύρω από το πιθανό μήκος κλειδιού
        if i > 12:
            break
        temp=0
        for x in range(i):
            temp=temp+coincidenceIndex(charText[x::(i)])
        meanIndexes.append(temp/(i)) #κρατάω τον μέσο δείκτη σύμπτωσης των διαφορετικών ομάδων
    keyLength=  meanIndexes.index(max(meanIndexes)) + 2 #παίρνω μήκος κλειδιού ίσο με αυτό που έχει τον μεγαλύτερο μέσο CI
    olis = 0
    for j in range(keyLength):
        if counter > 10:
            break
        shiftList= []
        list1=charText[j::keyLength]
        for i in range(keyLength): 
            if i == j:
                freq = [0]*26
                for t in list1:
                    freq[ord(t)-ord('A')]=freq[ord(t)-ord('A')]+1
                olis = freq.index(max(freq))
                olis = olis - 4
            list2=charText[i::keyLength]
            index=0
            shift=[]
            for k in range(26): #Βρίσκω για όλες τις ολισθήσεις τους CI και κρατάω τον καλύτερο
                index = coincidenceIndex(list2+list1)
                shift.append(index)
                for x in range(len(list2)):
                    list2[x] = chr(((ord(list2[x])-1)-ord('A'))%26+ord('A')) #ολισθαίνω κατα -1 την ομάδα γραμμάτων
            shiftList.append(shift.index(max(shift)))
        key=[0]
        for i in range(keyLength-1): #βρίσκω ένα πιθανό κλειδί που ικανοποίει τις ολισθήσεις
            key.append((shiftList[i+1]-shiftList[j])%26)
        for x in range(keyLength): #ολισθαίνω το κλειδί και το τυπώνω
            key[x] = (key[x]+olis)%26
            print(chr(key[x]+ord('A')), end="")
        print("")
        print("")
        i=0
        for t in charText:
            print(chr(((ord(t)-key[i%keyLength]-ord('A'))%26+ord('A'))), end="") #ολισθαίνω τα γράμματα ανάλογα με το κλειδί
            i=i+1
        counter += 1
        print("")
        print("")

vigenere("KUDLEZSIOGOOSMWJICKIELOLOVTDOECJZYWNCHIOAAKILDVUDWQIPJVKRPVLTLIOZATLJUCSMOIWLCKVBBLNZBJUCSMOIWLCKVURLYLZPZPFCVNDIYJLBENHEMCYWGVPFPAWUVHSUGQWCOBTOSFEPPEKPWLTSZZAOIIVUMCETWUPYOXGZAIONAHZCRNBIOFACMHOBIIVUJMEZPFIIEWWYMVPDAOJWFEWVWHYRQGKBIOTYZCCRWWOIUEVZZGPEYTSWFMPUCMOCBSKGIKCEEPPOZPGUTSWFMPUCFOFULEPPEZEEPPOZCYKIPAMABOYATSMTXAPESSQWCZPFSYSZCWYLXOSLTVENMIYBSPWQZWNYYRZEHNQDRFOFKLTVPDCIDQETWUOCEYQYEWVBKRPIXYGPETAJAEXQWOAOMMWOSFDOEXJFZAFORNZBEUUBULTSMXRQLOFOFNZXTJPLGZMDTWULHCVELXLOYYTLZCOMTGPTSGPYBFBKAJGZAISOAHPJZCAGBVMHPTIPZYBRNPTRLSOUADTTBQOQHRCWHYISOZEYBQUZURAHPICIPFBZEPAENMNKYKFXZTBIOWAEPZLBIOPNQQYOBFKUDSMMKVECFOFETZPISZMTOSZBIKAHTALXZPGZMLGRUAXSMTLVOLISVLTJWFXJFXKIYOTTBIOHRNPPXAIKUDMMQUZHVHDYMDYNPBLVPVLYPFVVVPAENMBBYOHBSGBGVPEDAZNMMYCEDIWYWURLBZEENIUSZSEIMRM")
