import os.path,csv,re
def mywrite(fw,s):
    s = s.replace("\n", "")
    l = re.findall("\d+\.\d+", s)
    temp = s.replace(str(l[0]), "", 1)
    if '\t' in temp: fw.write('"' + temp + '"')
    else: fw.write(temp)
def function(dir,outfile):
    scoresdir=dir+'/scores'
    sentdir=dir+'/sent'
    scoresitem = [d for d in os.listdir(scoresdir) if os.path.isdir(os.path.join(scoresdir, d))]
    sentitem = [d for d in os.listdir(sentdir) if os.path.isdir(os.path.join(sentdir, d))]
    fw=open(outfile,"w")
    quesfilepath = sentdir + '/questions'
    refansfilepath=sentdir+'/answers'
    qfr=open(quesfilepath,'r')
    rfr=open(refansfilepath,"r")
    for item in scoresitem:
        stuscorefilepath=scoresdir+'/'+item+'/ave'
        stuansfilepath=sentdir+'/'+item
        question=qfr.readline()
        refrence=rfr.readline()
        stuscore_fr=open(stuscorefilepath,"r")
        stuans_fr = open(stuansfilepath, "r")
        for temp in stuans_fr:
            if temp!="" and temp!="\n" :
                mywrite(fw,question)
                fw.write("\t")
                mywrite(fw,refrence)
                fw.write("\t")
                mywrite(fw,temp)
                fw.write('\t')
                fw.write(stuscore_fr.readline().replace("\n",""))
                fw.write('\n')
        stuscore_fr.close()
    qfr.close()
    rfr.close()
    fw.close()
workingdirectory="/home/batman/PycharmProjects/untitled"
opfile="output.csv"
function(workingdirectory,opfile)
with open(opfile,'rb') as tsvin:
     tsvin = csv.reader(tsvin, delimiter='\t')
     for row in tsvin:
         #print row[0],row[1],row[2],
        print  row[3]
