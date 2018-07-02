class Timer:
    def __init__(self, date, type):
        self.date_select = date
        self.type = type

    def get_code(self):
        date = self.date_select
        if(self.type == 'light'):
            codes = {'2018-06-17':'<img src="http://s.mmgo.io/t/_Hv" style="width: 100%" alt="motionmailapp.com" />', '2018-06-18':'<img src="http://s.mmgo.io/t/_Hy" style="width: 100%" alt="motionmailapp.com" />', '2018-06-19':'<img src="http://s.mmgo.io/t/_H0" style="width: 100%" alt="motionmailapp.com" />','2018-06-20':'<img src="https://s.mmgo.io/t/_cG" style="width: 100%" alt="motionmailapp.com" />','2018-06-20':'<img src="https://s.mmgo.io/t/_cG" style="width: 100%" alt="motionmailapp.com" />', '2018-06-21':'<img src="http://s.mmgo.io/t/_H1" style="width: 100%" alt="motionmailapp.com" />', '2018-06-22':'<img src="http://s.mmgo.io/t/_H2" style="width: 100%" alt="motionmailapp.com" />', '2018-06-23':'<img src="http://s.mmgo.io/t/_H3" style="width: 100%"  alt="motionmailapp.com" />', '2018-06-24':'<img src="https://s.mmgo.io/t/_cH" style="width: 100%" alt="motionmailapp.com" />', '2018-06-25':'<img src="http://s.mmgo.io/t/_H4" style="width: 100%" alt="motionmailapp.com" />', '2018-06-26':'<img src="http://s.mmgo.io/t/_H5" style="width: 100%" alt="motionmailapp.com" />','2018-06-27':'<img src="http://s.mmgo.io/t/_H7" style="width: 100%" alt="motionmailapp.com" />', '2018-06-28':'<img src="http://s.mmgo.io/t/_H8" style="width: 100%" alt="motionmailapp.com" />','2018-06-29':'<img src="http://s.mmgo.io/t/_H9" style="width: 100%" alt="motionmailapp.com" />', '2018-06-30':'<img src="http://s.mmgo.io/t/_H-" style="width: 100%" alt="motionmailapp.com" />', '2018-07-01':'<img src="https://s.mmgo.io/t/_bm" style="width: 100%" alt="motionmailapp.com" />', '2018-07-02':'<img src="https://s.mmgo.io/t/_bm" style="width: 100%" alt="motionmailapp.com" />', '2018-07-03':'<img src="https://s.mmgo.io/t/_bn" style="width: 100%" alt="motionmailapp.com" />', '2018-07-04':'<img src="https://s.mmgo.io/t/_bo" style="width: 100%" alt="motionmailapp.com" />','2018-07-05':'<img src="https://s.mmgo.io/t/_bp" style="width: 100%" alt="motionmailapp.com" />','2018-07-06':'<img src="https://s.mmgo.io/t/_bq" style="width: 100%" alt="motionmailapp.com" />', '2018-07-07':'<img src="https://s.mmgo.io/t/_br" style="width: 100%" alt="motionmailapp.com" />', '2018-07-08':'<img src="https://s.mmgo.io/t/_bs" style="width: 100%" alt="motionmailapp.com" />','2018-07-09':'<img src="https://s.mmgo.io/t/_bt" style="width: 100%" alt="motionmailapp.com" />', '2018-07-10':'<img src="https://s.mmgo.io/t/_bu" style="width: 100%" alt="motionmailapp.com" />', '2018-07-11':'<img src="https://s.mmgo.io/t/_bu" style="width: 100%" alt="motionmailapp.com" />', '2018-07-12':'<img src="https://s.mmgo.io/t/_l-" style="width: 100%" alt="motionmailapp.com" />', '2018-07-13':'<img src="https://s.mmgo.io/t/_l7" style="width: 100%" alt="motionmailapp.com" />','2018-07-14':'<img src="https://s.mmgo.io/t/_mB" style="width: 100%" alt="motionmailapp.com" />', '2018-07-15':'<img src="https://s.mmgo.io/t/_mC" style="width: 100%" alt="motionmailapp.com" />', '2018-07-16':'<img src="https://s.mmgo.io/t/_mG" style="width: 100%" alt="motionmailapp.com" />', '2018-07-17':'<img src="https://s.mmgo.io/t/_mH" style="width: 100%" alt="motionmailapp.com" />', '2018-07-18':'<img src="https://s.mmgo.io/t/_mJ" style="width: 100%" alt="motionmailapp.com" />', '2018-07-19':'<img src="https://s.mmgo.io/t/_mL" style="width: 100%" alt="motionmailapp.com" />', '2018-07-20':'<img src="https://s.mmgo.io/t/_mM" style="width: 100%" alt="motionmailapp.com" />', '2018-07-21':'<img src="https://s.mmgo.io/t/_mP" style="width: 100%" alt="motionmailapp.com" />', '2018-07-22':'<img src="https://s.mmgo.io/t/_mQ" style="width: 100%" alt="motionmailapp.com" />', '2018-07-23':'<img src="https://s.mmgo.io/t/_mR" style="width: 100%" alt="motionmailapp.com" />', '2018-07-24':'<img src="https://s.mmgo.io/t/_mS" style="width: 100%" alt="motionmailapp.com" />', '2081-07-25':'<img src="https://s.mmgo.io/t/_mU" style="width: 100%" alt="motionmailapp.com" />', '2018-07-26':'<img src="https://s.mmgo.io/t/_mV" style="width: 100%" alt="motionmailapp.com" />', '2018-07-27':'<img src="https://s.mmgo.io/t/_mW" style="width: 100%" alt="motionmailapp.com" />', '2018-07-28':'<img src="https://s.mmgo.io/t/_mX" style="width: 100%" alt="motionmailapp.com" />', '2018-07-29':'<img src="https://s.mmgo.io/t/_mZ" style="width: 100%" alt="motionmailapp.com" />', '2018-07-30':'<img src="https://s.mmgo.io/t/_ma" style="width: 100%" alt="motionmailapp.com" />', '2018-07-31':'<img src="https://s.mmgo.io/t/_me" style="width: 100%" alt="motionmailapp.com" />'}
            return codes.get(date)

        elif(self.type == 'dark'):
            codes = {'2018-06-18':'<img src="https://s.mmgo.io/t/_bI" style="width:90%" alt="motionmailapp.com" />', '2018-06-19':'<img src="https://s.mmgo.io/t/_bJ" style="width:90%" alt="motionmailapp.com" />', '2018-06-20':'<img src="https://s.mmgo.io/t/_bK" style="width: 90%" alt="motionmailapp.com" />','2018-06-21':'<img src="https://s.mmgo.io/t/_bL" style="width: 90%" alt="motionmailapp.com" />', '2018-06-22':'<img src="https://s.mmgo.io/t/_bM" style="width: 90%" alt="motionmailapp.com" />', '2018-06-23':'<img src="https://s.mmgo.io/t/_bO" style="width: 90%" alt="motionmailapp.com" />','2018-06-24':'<img src="https://s.mmgo.io/t/_bP" style="width: 90%" alt="motionmailapp.com" />', '2018-06-25':'<img src="https://s.mmgo.io/t/_bQ" style="width: 90%" alt="motionmailapp.com" />', '2018-06-26':'<img src="https://s.mmgo.io/t/_bS" style="width: 90%" alt="motionmailapp.com" />','2018-06-27':'<img src="https://s.mmgo.io/t/_bT" style="width: 90%" alt="motionmailapp.com" />','2018-06-28':'<img src="https://s.mmgo.io/t/_bU" style="width: 90%" alt="motionmailapp.com" />', '2018-06-29':'<img src="https://s.mmgo.io/t/_bV" style="width: 90%" alt="motionmailapp.com" />', '2018-06-30':'<img src="https://s.mmgo.io/t/_bW" style="width: 90%" alt="motionmailapp.com" />', '2018-07-01':'<img src="https://s.mmgo.io/t/_bY" style="width:90%" alt="motionmailapp.com" />', '2018-07-02':'<img src="https://s.mmgo.io/t/_bZ" style="width: 90%" alt="motionmailapp.com" />', '2018-07-03':'<img src="https://s.mmgo.io/t/_ba" style="width: 90%" alt="motionmailapp.com" />', '2018-07-04':'<img src="https://s.mmgo.io/t/_bc" style="width: 90%" alt="motionmailapp.com" />', '2018-07-05':'<img src="https://s.mmgo.io/t/_bd" style="width: 90%" alt="motionmailapp.com" />', '2018-07-06':'<img src="https://s.mmgo.io/t/_be" style="width: 90%"  alt="motionmailapp.com" />', '2018-07-07':'<img src="https://s.mmgo.io/t/_bf" style="width: 90%" alt="motionmailapp.com" />', '2018-07-08':'<img src="https://s.mmgo.io/t/_bg" style="width: 90%" alt="motionmailapp.com" />', '2018-07-09':'<img src="https://s.mmgo.io/t/_bj" style="width: 90%" alt="motionmailapp.com" />', '2018-07-10':'<img src="https://s.mmgo.io/t/_bh" style="width: 90%" alt="motionmailapp.com" />', '2018-07-11':'<img src="https://s.mmgo.io/t/_mi" style="width: 90%" alt="motionmailapp.com" />', '2018-07-12':'<img src="https://s.mmgo.io/t/_ml" style="width: 90%" alt="motionmailapp.com" />', '2018-07-13':'<img src="https://s.mmgo.io/t/_mm" style="width: 90%" alt="motionmailapp.com" />', '2018-07-14':'<img src="https://s.mmgo.io/t/_mo" style="width: 90%" alt="motionmailapp.com" />', '2018-07-15':'<img src="https://s.mmgo.io/t/_mp" style="width:90%" alt="motionmailapp.com" />', '2018-07-16':'<img src="https://s.mmgo.io/t/_mq" style="width: 90%" alt="motionmailapp.com" />', '2018-07-17':'<img src="https://s.mmgo.io/t/_mr" style="width: 90%" alt="motionmailapp.com" />', '2018-07-18':'<img src="https://s.mmgo.io/t/_mt" style="width: 90%" alt="motionmailapp.com" />', '2018-07-19':'<img src="https://s.mmgo.io/t/_mu" style="width: 90%" alt="motionmailapp.com" />', '2018-07-20':'<img src="https://s.mmgo.io/t/_mv" style="width: 90%" alt="motionmailapp.com" />', '2018-07-21':'<img src="https://s.mmgo.io/t/_mw" style="width: 90%" alt="motionmailapp.com" />', '2018-07-22':'<img src="https://s.mmgo.io/t/_oJ" style="width: 90%" alt="motionmailapp.com" />', '2018-07-23':'<img src="https://s.mmgo.io/t/_oK" style="width: 90%" alt="motionmailapp.com" />', '2018-07-24':'<img src="https://s.mmgo.io/t/_oL" style="width: 90%" alt="motionmailapp.com" />', '2018-07-25':'<img src="https://s.mmgo.io/t/_oM" style="width: 90%" alt="motionmailapp.com" />', '2018-07-26':'<img src="https://s.mmgo.io/t/_oN" style="width: 90%" alt="motionmailapp.com" />', '2018-07-27':'<img src="https://s.mmgo.io/t/_oO" style="width: 90%" alt="motionmailapp.com" />', '2018-07-28':'<img src="https://s.mmgo.io/t/_oP" style="width: 90%" alt="motionmailapp.com" />', '2018-07-29':'<img src="https://s.mmgo.io/t/_oQ" style="width: 90%" alt="motionmailapp.com" />', '2018-07-30':'<img src="https://s.mmgo.io/t/_oR" style="width: 90%" alt="motionmailapp.com" />', '2018-07-31':'<img src="https://s.mmgo.io/t/_oS" style="width: 90%" alt="motionmailapp.com" />'}
            return codes.get(date)