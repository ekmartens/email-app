from flask import Flask, render_template, send_file, request
from backend import Templates
from timer import Timer
import webbrowser

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', font_url='https://fonts.googleapis.com/css?family=Bungee+Shade')

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        emails = Templates()
        logo1=request.form["event_logo"]
        location=request.form["event_location"]
        event_day=request.form["day"]
        name=request.form["event_name"]
        code=request.form["pre_offer_code"]
        sport=request.form["sport_choice"]
        expire1=request.form["pre_promo_expire"]
        plogo=request.form["partner_logo"]
        expire2=request.form["post_promo_expire"]
        code2=request.form["post_promo"]
        est_deliver_date=request.form["eta_date"]
        video_link=request.form["video"]
        video_img_link=request.form["vid_thumb"]
        video_title=request.form["vid_title"]

        #new code
        pre_timer_picker=request.form["pre_timer_picker"]
        pre_timer_select = Timer(pre_timer_picker, 'light')
        pre_timer = str(pre_timer_select.get_code())

        post_timer_picker=request.form["post_timer_picker"]
        post_timer_select = Timer(post_timer_picker, 'light')
        post_timer = str(post_timer_select.get_code())

        coupon_timer_picker=request.form["coupon_timer_picker"]
        coupon_timer_select = Timer(coupon_timer_picker, 'dark')
        dark_timer = str(coupon_timer_select.get_code())

        pre_coupon_timer=request.form["pre_coupon_picker"]
        pre_coupon_timer_select = Timer(pre_coupon_timer, 'dark')
        pre_dark_timer = str(pre_coupon_timer_select.get_code())

        code6a=request.form["6a_promo"]

        #end new code

        emails.create_templates(logo1, location, event_day, name, sport, code, expire1, plogo, pre_timer, post_timer, dark_timer, expire2, code2, est_deliver_date, video_link, video_img_link, video_title, pre_dark_timer, code6a)
        if(sport=="Lacrosse"):
            return render_template('success.html', font_url='https://fonts.googleapis.com/css?family=Bungee+Shade')
        elif(sport == "Softball"):
            return render_template('success-softball.html', font_url='https://fonts.googleapis.com/css?family=Bungee+Shade')
        elif(sport == "Baseball"):
            return render_template('success-baseball.html', font_url='https://fonts.googleapis.com/css?family=Bungee+Shade')
        elif(sport == "Soccer"):
            return render_template('success-soccer.html', font_url='https://fonts.googleapis.com/css?family=Bungee+Shade')
        else:
            return 'Templates for ' + sport + ' will be available when complete.'

#lacrosse emails
@app.route("/view", methods=['POST'])
def view():
	try:
		return send_file('emails/lacrosse1.txt', attachment_filename='lacrosse1.txt')
	except Exception as e:
		return str(e)

@app.route("/preview1")
def preview1():
    return render_template('lacrosse1.html')

@app.route("/view1a", methods=['POST'])
def view1a():
	try:
		return send_file('emails/lacrosse1a.txt', attachment_filename='lacrosse1a.txt')
	except Exception as e:
		return str(e)

@app.route("/preview1a")
def preview1a():
    return render_template('lacrosse1a.html')

@app.route("/view2", methods=['POST'])
def view2():
	try:
		return send_file('emails/lacrosse2.txt', attachment_filename='lacrosse2.txt')
	except Exception as e:
		return str(e)

@app.route("/preview2")
def preview2():
    return render_template('lacrosse2.html')

@app.route("/view3a", methods=['POST'])
def view3a():
	try:
		return send_file('emails/lacrosse3a.txt', attachment_filename='lacrosse3a.txt')
	except Exception as e:
		return str(e)

@app.route("/preview3a")
def preview3a():
    return render_template('lacrosse3a.html')

@app.route("/view3", methods=['POST'])
def view3():
	try:
		return send_file('emails/lacrosse3.txt', attachment_filename='lacrosse3.txt')
	except Exception as e:
		return str(e)

@app.route("/preview3")
def preview3():
    return render_template('lacrosse3.html')

@app.route("/view4", methods=['POST'])
def view4():
	try:
		return send_file('emails/lacrosse4.txt', attachment_filename='lacrosse4.txt')
	except Exception as e:
		return str(e)

@app.route("/preview4")
def preview4():
    return render_template('lacrosse4.html')

@app.route("/view5a", methods=['POST'])
def view5a():
	try:
		return send_file('emails/lacrosse5a.txt', attachment_filename='lacrosse5a.txt')
	except Exception as e:
		return str(e)

@app.route("/preview5a")
def preview5a():
    return render_template('lacrosse5a.html')

@app.route("/view5", methods=['POST'])
def view5():
	try:
		return send_file('emails/lacrosse5.txt', attachment_filename='lacrosse5.txt')
	except Exception as e:
		return str(e)

@app.route("/preview5")
def preview5():
    return render_template('lacrosse5.html')

@app.route("/view6b", methods=['POST'])
def view6b():
	try:
		return send_file('emails/lacrosse6b.txt', attachment_filename='lacrosse6b.txt')
	except Exception as e:
		return str(e)

@app.route("/preview6b")
def preview6b():
    return render_template('lacrosse6b.html')

@app.route("/view6", methods=['POST'])
def view6():
	try:
		return send_file('emails/lacrosse6.txt', attachment_filename='lacrosse6.txt')
	except Exception as e:
		return str(e)

@app.route("/preview6")
def preview6():
    return render_template('lacrosse6.html')

@app.route("/view6a", methods=['POST'])
def view6a():
	try:
		return send_file('emails/lacrosse6a.txt', attachment_filename='lacrosse6a.txt')
	except Exception as e:
		return str(e)

@app.route("/preview6a")
def preview6a():
    return render_template('lacrosse6a.html')

@app.route("/view7", methods=['POST'])
def view7():
	try:
		return send_file('emails/lacrosse7.txt', attachment_filename='lacrosse7.txt')
	except Exception as e:
		return str(e)

@app.route("/preview7")
def preview7():
    return render_template('lacrosse7.html')

@app.route("/view8", methods=['POST'])
def view8():
	try:
		return send_file('emails/lacrosse8.txt', attachment_filename='lacrosse8.txt')
	except Exception as e:
		return str(e)

@app.route("/preview8")
def preview8():
    return render_template('lacrosse8.html')

#softball emails

@app.route("/softball_view1", methods=['POST'])
def softball_view1():
	try:
		return send_file('emails/softball1.txt', attachment_filename='softball1.txt')
	except Exception as e:
		return str(e)

@app.route("/softball_preview1")
def softball_preview1():
    return render_template('softball1.html')

@app.route("/softball_view2", methods=['POST'])
def softball_view2():
	try:
		return send_file('emails/softball2.txt', attachment_filename='softball2.txt')
	except Exception as e:
		return str(e)

@app.route("/softball_preview2")
def softball_preview2():
    return render_template('softball2.html')

@app.route("/softball_view3", methods=['POST'])
def softball_view3():
	try:
		return send_file('emails/softball3.txt', attachment_filename='softball3.txt')
	except Exception as e:
		return str(e)

@app.route("/softball_preview3")
def softball_preview3():
    return render_template('softball3.html')

@app.route("/softball_view4", methods=['POST'])
def softball_view4():
	try:
		return send_file('emails/softball4.txt', attachment_filename='softball4.txt')
	except Exception as e:
		return str(e)

@app.route("/softball_preview4")
def softball_preview4():
    return render_template('softball4.html')

@app.route("/softball_view5a", methods=['POST'])
def softball_view5a():
	try:
		return send_file('emails/softball5a.txt', attachment_filename='softball5a.txt')
	except Exception as e:
		return str(e)

@app.route("/softball_preview5a")
def softball_preview5a():
    return render_template('softball5a.html')

@app.route("/softball_view5", methods=['POST'])
def softball_view5():
	try:
		return send_file('emails/softball5.txt', attachment_filename='softball5.txt')
	except Exception as e:
		return str(e)

@app.route("/softball_preview5")
def softball_preview5():
    return render_template('softball5.html')

@app.route("/softball_view6", methods=['POST'])
def softball_view6():
	try:
		return send_file('emails/softball6.txt', attachment_filename='softball6.txt')
	except Exception as e:
		return str(e)

@app.route("/softball_preview6")
def softball_preview6():
    return render_template('softball6.html')

@app.route("/softball_view7", methods=['POST'])
def softball_view7():
	try:
		return send_file('emails/softball7.txt', attachment_filename='softball7.txt')
	except Exception as e:
		return str(e)

@app.route("/softball_preview7")
def softball_preview7():
    return render_template('softball7.html')

#baseball emails

@app.route("/baseball_view1", methods=['POST'])
def baseball_view1():
	try:
		return send_file('emails/baseball1.txt', attachment_filename='baseball1.txt')
	except Exception as e:
		return str(e)

@app.route("/baseball_preview1")
def baseball_preview1():
    return render_template('baseball1.html')

@app.route("/baseball_view2", methods=['POST'])
def baseball_view2():
	try:
		return send_file('emails/baseball2.txt', attachment_filename='baseball2.txt')
	except Exception as e:
		return str(e)

@app.route("/baseball_preview2")
def baseball_preview2():
    return render_template('baseball2.html')

@app.route("/baseball_view3", methods=['POST'])
def baseball_view3():
	try:
		return send_file('emails/baseball3.txt', attachment_filename='baseball3.txt')
	except Exception as e:
		return str(e)

@app.route("/baseball_preview3")
def baseball_preview3():
    return render_template('baseball3.html')

@app.route("/baseball_view4", methods=['POST'])
def baseball_view4():
	try:
		return send_file('emails/baseball4.txt', attachment_filename='baseball4.txt')
	except Exception as e:
		return str(e)

@app.route("/baseball_preview4")
def baseball_preview4():
    return render_template('baseball4.html')

@app.route("/baseball_view5a", methods=['POST'])
def baseball_view5a():
	try:
		return send_file('emails/baseball5a.txt', attachment_filename='baseball5a.txt')
	except Exception as e:
		return str(e)

@app.route("/baseball_preview5a")
def baseball_preview5a():
    return render_template('baseball5a.html')

@app.route("/baseball_view5", methods=['POST'])
def baseball_view5():
	try:
		return send_file('emails/baseball5.txt', attachment_filename='baseball5.txt')
	except Exception as e:
		return str(e)

@app.route("/baseball_preview5")
def baseball_preview5():
    return render_template('baseball5.html')

@app.route("/baseball_view6", methods=['POST'])
def baseball_view6():
	try:
		return send_file('emails/baseball6.txt', attachment_filename='baseball6.txt')
	except Exception as e:
		return str(e)

@app.route("/baseball_preview6")
def baseball_preview6():
    return render_template('baseball6.html')

@app.route("/baseball_view7", methods=['POST'])
def baseball_view7():
	try:
		return send_file('emails/baseball7.txt', attachment_filename='baseball7.txt')
	except Exception as e:
		return str(e)

@app.route("/baseball_preview7")
def baseball_preview7():
    return render_template('baseball7.html')

#soccer emails

@app.route("/soccer_view1", methods=['POST'])
def soccer_view1():
	try:
		return send_file('emails/soccer1.txt', attachment_filename='soccer1.txt')
	except Exception as e:
		return str(e)

@app.route("/soccer_preview1")
def soccer_preview1():
    return render_template('soccer1.html')

@app.route("/soccer_view2", methods=['POST'])
def soccer_view2():
	try:
		return send_file('emails/soccer2.txt', attachment_filename='soccer2.txt')
	except Exception as e:
		return str(e)

@app.route("/soccer_preview2")
def soccer_preview2():
    return render_template('soccer2.html')

@app.route("/soccer_view3", methods=['POST'])
def soccer_view3():
	try:
		return send_file('emails/soccer3.txt', attachment_filename='soccer3.txt')
	except Exception as e:
		return str(e)

@app.route("/soccer_preview3")
def soccer_preview3():
    return render_template('soccer3.html')

@app.route("/soccer_view4", methods=['POST'])
def soccer_view4():
	try:
		return send_file('emails/soccer4.txt', attachment_filename='soccer4.txt')
	except Exception as e:
		return str(e)

@app.route("/soccer_preview4")
def soccer_preview4():
    return render_template('soccer4.html')

@app.route("/soccer_view5a", methods=['POST'])
def soccer_view5a():
	try:
		return send_file('emails/soccer5a.txt', attachment_filename='soccer5a.txt')
	except Exception as e:
		return str(e)

@app.route("/soccer_preview5a")
def soccer_preview5a():
    return render_template('soccer5a.html')

@app.route("/soccer_view5", methods=['POST'])
def soccer_view5():
	try:
		return send_file('emails/soccer5.txt', attachment_filename='soccer5.txt')
	except Exception as e:
		return str(e)

@app.route("/soccer_preview5")
def soccer_preview5():
    return render_template('soccer5.html')

@app.route("/soccer_view6", methods=['POST'])
def soccer_view6():
	try:
		return send_file('emails/soccer6.txt', attachment_filename='soccer6.txt')
	except Exception as e:
		return str(e)

@app.route("/soccer_preview6")
def soccer_preview6():
    return render_template('soccer6.html')

@app.route("/soccer_view7", methods=['POST'])
def soccer_view7():
	try:
		return send_file('emails/soccer7.txt', attachment_filename='soccer7.txt')
	except Exception as e:
		return str(e)

@app.route("/soccer_preview7")
def soccer_preview7():
    return render_template('soccer7.html')


if __name__ == '__main__':
    app.run(debug=True)
