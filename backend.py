class Templates:
    def __init__(self):
        self.name = self

    def create_templates(self, event_logo, location, date, event, sport, code, pre_expire, plogo, pre_timer, post_timer, dark_timer, expire2, code2, estimate, video, video_img, vid_title, pre_dark_timer, code6a):
        #variables for front end input
        sport_selection = sport
        header_event_logo = event_logo
        event_location = location
        event_date = date
        event_name = event
        discount_code = code
        partner_logo = plogo
        pre_expiration_date = pre_expire
        pre_event_timer = pre_timer
        pre_event_coupon_timer = pre_dark_timer
        post_event_timer1 = post_timer
        post_event_timer_black_background = dark_timer
        post_code_expiration = expire2
        post_event_promo_code = code2
        estimated_delivery = estimate
        video_link = video
        video_alt_img = video_img
        video_title = vid_title
        coupon_code6a = code6a


        #VARIABLES FOR TEMPLATE PARTS

        #variable for the rest of the header
        finish_header = "<img src=\"" + header_event_logo + "\" style=\"width:90%\">\n<p style=\"text-align: center; color: #fff; line-height: .75; font-family: Lato, Arial; font-size: 28pt;\"><strong>" + event_location + "</strong></p>\n<p style=\"text-align: center; color: #fff; line-height: .75; font-family: Lato, Arial; font-size: 28pt;\"><strong>" + event_date + "</strong></p>\n</td>\n</tr>\n</tbody>\n</table>\n</div>\n<style>\n@media all and\n(max-width: 450px){\n.header-table {\nmax-width: 300px;\n}\n}\n</style>\n</td>\n</tr>\n</tbody>\n</table></td>\n</tr>\n</table>\n<!--[if (gte mso 9)|(IE)]>\n</td>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>"

        #Email Template 1a

        email1a_top = '<tr>\n<td align="center" valign="top" id="templateBody" data-template-container>\n<!--[if (gte mso 9)|(IE)]>\n<table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">\n<tr>\n<td align="center" valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">\n<tr>\n<td valign="top" class="bodyContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding: 0px 18px 9px; line-height: 200%;">\n<p style="text-align: center; line-height: 200%;"><font color="#000000" face="lato, helvetica neue, helvetica, arial, sans-serif"><span style="font-size:20px"><strong>Congratulations! You\'re one of the first to register.</strong></span></font><br>\n<strong><span style="color:#000000"><span style="font-size:20px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif">Lock in Early Bird savings on Unlimited Highlight Reels!</span></span></span></strong></p>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        email1a_timer_coupon = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCodeBlock">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner">\n<div class="mcnTextContent">\n<div align="center" style="background: #000; padding-top: 15px; padding-bottom: 30px;">\n<a href="https://nextpro.com/subscriptions.html#level" target="_blank"><img src="https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/21bbd825-d090-4f41-8799-ffb9a021235e.png" style="width: 40%; padding:2%" alt="Logo"></a>\n<h1 style="color:#fff; font-family: Lato; text-align: center;font-size: 42pt">Game Film + Highlights</h1>\n' + pre_event_coupon_timer + '\n<p style="color:#fff; font-family: Lato; text-align: center; font-size: 28pt">Use code <span style="color:#ff2a03">' + discount_code + '</span> for 15% off.</p>\n<table>\n<tbody>\n<tr>\n<td align="center" style="width: 200px; height: 45px; background: #28a9ff; border-radius: 5px">\n<a href="https://nextpro.com/subscriptions.html#level" style="color: #fff; text-decoration: none; font-family: Lato; font-size: 18pt;" target="_blank">Subscribe</a>\n</td>\n</tr>\n</tbody>\n</table><table>\n</table></div></div></td></tr></tbody></table>'

        email1a_testimonials = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock" style="min-width:100%;">\n<tbody class="mcnImageBlockOuter">\n<tr>\n<td valign="top" style="padding:9px" class="mcnImageBlockInner">\n<table align="left" width="100%" border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="min-width:100%;">\n<tbody><tr>\n<td class="mcnImageContent" valign="top" style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0; text-align:center;">\n<img align="center" alt="" src="https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/850495a0-abb1-4450-8688-2dba09c99165.png" width="564" style="max-width:686px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" class="mcnImage">\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody>\n</table></td>\n</tr>\n</table>\n<!--[if (gte mso 9)|(IE)]>\n</td>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>'

        #Email 1 Template

        email1_section1 = "<tr>\n<td align=\"center\" valign=\"top\" id=\"templateBody\" data-template-container>\n<!--[if (gte mso 9)|(IE)]>\n<table align=\"center\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"600\" style=\"width:600px;\">\n<tr>\n<td align=\"center\" valign=\"top\" width=\"600\" style=\"width:600px;\">\n<![endif]-->\n<table align=\"center\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"templateContainer\">\n<tr>\n<td valign=\"top\" class=\"bodyContainer\"><table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnTextBlock\" style=\"min-width:100%;\">\n<tbody class=\"mcnTextBlockOuter\">\n<tr>\n<td valign=\"top\" class=\"mcnTextBlockInner\" style=\"padding-top:9px;\">\n<!--[if mso]>\n<table align=\"left\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\" style=\"width:100%;\">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign=\"top\" width=\"600\" style=\"width:600px;\">\n<![endif]-->\n<table align=\"left\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" style=\"max-width:100%; min-width:100%;\" width=\"100%\" class=\"mcnTextContentContainer\">\n<tbody><tr>\n<td valign=\"top\" class=\"mcnTextContent\" style=\"padding: 0px 18px 9px; line-height: 200%;\">\n<p style=\"text-align: center; line-height: 200%;\"><span style=\"font-size:20px\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\"><strong><span style=\"color:#000000\">Get Unlimited Game Film Downloads and Highlight Reels</span></strong></span></span><br><font color=\"#000000\" face=\"lato, helvetica neue, helvetica, arial, sans-serif\"><span style=\"font-size:20px\"><strong>For</strong></span></font><span style=\"color:#0000FF\"><font face=\"lato, helvetica neue, helvetica, arial, sans-serif\"><span style=\"font-size:20px\"><strong> " +  event_name + "</strong></span></font></span></p>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnDividerBlock\" style=\"min-width:100%;\">\n<tbody class=\"mcnDividerBlockOuter\">\n<tr>\n<td class=\"mcnDividerBlockInner\" style=\"min-width:100%; padding:18px;\">\n<table class=\"mcnDividerContent\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" style=\"min-width: 100%;border-top: 2px solid #EAEAEA;\">\n<tbody><tr>\n<td>\n<span></span>\n</td>\n</tr>\n</tbody></table>\n<!--\n<td class=\"mcnDividerBlockInner\" style=\"padding: 18px;\">\n<hr class=\"mcnDividerContent\" style=\"border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;\" />\n-->\n</td>\n</tr>\n</tbody>\n</table>"

        #coupon: Lacrosse
        coupon_lacrosse = "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnCodeBlock\">\n<tbody class=\"mcnTextBlockOuter\">\n<tr>\n<td valign=\"top\" class=\"mcnTextBlockInner\">\n<div class=\"mcnTextContent\"><div align=\"center\" style=\"background: #000; padding-top: 15px; padding-bottom: 30px;\">\n<a href=\"https://nextpro.com/subscriptions.html#level\" target=\"_blank\"><img src=\"https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/21bbd825-d090-4f41-8799-ffb9a021235e.png\" style=\"width: 40%; padding:2%\" alt=\"Logo\"></a>\n<h1 style=\"color:#fff; font-family: Lato; text-align: center;font-size: 42pt\">Game Film + Highlights</h1><p style=\"color:#fff; font-family: Lato; text-align: center; font-size: 28pt\">Use code <span style=\"color:#ff2a03\">" + discount_code + "</span> for 15% off.</p>\n<table>\n<tbody>\n<tr>\n<td align=\"center\" style=\"width: 200px; height: 45px; background: #28a9ff; border-radius: 5px\">\n<a href=\"https://nextpro.com/subscriptions.html#level\" style=\"color: #fff; text-decoration: none; font-family: Lato; font-size: 18pt;\" target=\"_blank\">Subscribe</a>\n</td>\n</tr>\n</tbody>\n</table><table>\n</table></div></div></td></tr></tbody></table>"

        #coupon Baseball/Softball

        coupon_basesoft = "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnCodeBlock\">\n<tbody class=\"mcnTextBlockOuter\">\n<tr>\n<td valign=\"top\" class=\"mcnTextBlockInner\">\n<div class=\"mcnTextContent\"><div align=\"center\" style=\"background: #000; padding-top: 15px; padding-bottom: 30px;\">\n<a href=\"https://nextpro.com/subscriptions.html#level\" target=\"_blank\"><img src=\"https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/21bbd825-d090-4f41-8799-ffb9a021235e.png\" style=\"width: 40%; padding:2%\" alt=\"Logo\"></a>\n<h1 style=\"color:#fff; font-family: Lato; text-align: center;font-size: 42pt\">Got Highlight Reels?</h1><p style=\"color:#fff; font-family: Lato; text-align: center; font-size: 28pt\">Use code <span style=\"color:#ff2a03\">" + discount_code + "</span> for $100 off.</p>\n<table>\n<tbody>\n<tr>\n<td align=\"center\" style=\"width: 200px; height: 45px; background: #28a9ff; border-radius: 5px\">\n<a href=\"https://nextpro.com/subscriptions.html#level\" style=\"color: #fff; text-decoration: none; font-family: Lato; font-size: 18pt;\" target=\"_blank\">Subscribe</a>\n</td>\n</tr>\n</tbody>\n</table><table>\n</table></div></div></td></tr></tbody></table>"

        #coupon: Soccer
        coupon1_soccer = "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnCodeBlock\">\n<tbody class=\"mcnTextBlockOuter\">\n<tr>\n<td valign=\"top\" class=\"mcnTextBlockInner\">\n<div class=\"mcnTextContent\"><div align=\"center\" style=\"background: #000; padding-top: 15px; padding-bottom: 30px;\">\n<a href=\"https://nextpro.com/subscriptions.html#level\" target=\"_blank\"><img src=\"https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/21bbd825-d090-4f41-8799-ffb9a021235e.png\" style=\"width: 40%; padding:2%\" alt=\"Logo\"></a>\n<h1 style=\"color:#fff; font-family: Lato; text-align: center;font-size: 42pt\">Game Film + Highlights</h1><p style=\"color:#fff; font-family: Lato; text-align: center; font-size: 28pt\">Use code <span style=\"color:#ff2a03\">" + discount_code + "</span> for $100 off.</p>\n<table>\n<tbody>\n<tr>\n<td align=\"center\" style=\"width: 200px; height: 45px; background: #28a9ff; border-radius: 5px\">\n<a href=\"https://nextpro.com/subscriptions.html#level\" style=\"color: #fff; text-decoration: none; font-family: Lato; font-size: 18pt;\" target=\"_blank\">Subscribe</a>\n</td>\n</tr>\n</tbody>\n</table><table>\n</table></div></div></td></tr></tbody></table>"

        #post-event coupon: Lacrosse

        post_event_coupon_lacrosse = "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnCodeBlock\">\n<tbody class=\"mcnTextBlockOuter\">\n<tr>\n<td valign=\"top\" class=\"mcnTextBlockInner\">\n<div class=\"mcnTextContent\"><div align=\"center\" style=\"background: #000; padding-top: 15px; padding-bottom: 30px;\">\n<a href=\"https://nextpro.com/subscriptions.html#level\" target=\"_blank\"><img src=\"https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/21bbd825-d090-4f41-8799-ffb9a021235e.png\" style=\"width: 40%; padding:2%\" alt=\"Logo\"></a>\n<h1 style=\"color:#fff; font-family: Lato; text-align: center;font-size: 42pt\">Game Film + Highlights</h1><p style=\"color:#fff; font-family: Lato; text-align: center; font-size: 28pt\">Use code <span style=\"color:#ff2a03\">" + post_event_promo_code + "</span> for 10% off.</p>\n<table>\n<tbody>\n<tr>\n<td align=\"center\" style=\"width: 200px; height: 45px; background: #28a9ff; border-radius: 5px\">\n<a href=\"https://nextpro.com/subscriptions.html#level\" style=\"color: #fff; text-decoration: none; font-family: Lato; font-size: 18pt;\" target=\"_blank\">Subscribe</a>\n</td>\n</tr>\n</tbody>\n</table><table>\n</table></div></div></td></tr></tbody></table>"

        #caveat block

        caveat = "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnTextBlock\" style=\"min-width:100%;\">\n<tbody class=\"mcnTextBlockOuter\">\n<tr>\n<td valign=\"top\" class=\"mcnTextBlockInner\" style=\"padding-top:9px;\">\n<!--[if mso]>\n<table align=\"left\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\" style=\"width:100%;\">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign=\"top\" width=\"600\" style=\"width:600px;\">\n<![endif]-->\n<table align=\"left\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" style=\"max-width:100%; min-width:100%;\" width=\"100%\" class=\"mcnTextContentContainer\">\n<tbody><tr>\n<td valign=\"top\" class=\"mcnTextContent\" style=\"padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;\">\n<div style=\"text-align: center;\"><span style=\"font-size:20px\"><span style=\"color:#000000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif; line-height:1.25\">Save 15%. Use code</span></span><span style=\"color:#FF0000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\"> </span></span><span style=\"color:#3d65b0\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\">" + discount_code + " </span></span><span style=\"color:#FF0000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\"> </span></span><span style=\"color:#000000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\">at checkout.</span></span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>"

        divider = "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnDividerBlock\" style=\"min-width:100%;\"><tbody class=\"mcnDividerBlockOuter\">\n<tr>\n<td class=\"mcnDividerBlockInner\" style=\"min-width:100%; padding:18px;\">\n<table class=\"mcnDividerContent\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" style=\"min-width: 100%;border-top: 2px solid #EAEAEA;\">\n<tbody><tr>\n<td>\n<span></span>\n</td>\n</tr>\n</tbody></table>\n<!-- \n<td class=\"mcnDividerBlockInner\" style=\"padding: 18px;\">\n<hr class=\"mcnDividerContent\" style=\"border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;\" />\n-->\n</td>\n</tr>\n</tbody>\n</table>"

        unlimited_game_film = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageCardBlock">\n<tbody class="mcnImageCardBlockOuter"><tr>\n<td class="mcnImageCardBlockInner" valign="top" style="padding-top:9px; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<table border="0" cellpadding="0" cellspacing="0" class="mcnImageCardLeftContentOuter" width="100%">\n<tbody><tr>\n<td align="center" valign="top" class="mcnImageCardLeftContentInner" style="padding:0;">\n<table align="right" border="0" cellpadding="0" cellspacing="0" class="mcnImageCardLeftImageContentContainer" width="282">\n<tbody><tr>\n<td class="mcnImageCardLeftImageContentE2E " align="left" valign="top" style="padding-top:0px; padding-right:0px; padding-bottom:0px; padding-left:0;">\n<a href="https://nextpro.com/subscriptions.html#level" title="" class="" target="_blank">\n<img alt="" src="https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/8100fcee-68e7-4b02-9f5b-bc5d4b4e011b.png" width="282" style="max-width:650px;" class="mcnImage"></a>\n</td>\n</tr>\n</tbody></table>\n<table class="mcnImageCardLeftTextContentContainer" align="left" border="0" cellpadding="0" cellspacing="0" width="264">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-left: 18px;padding-top: 18px;padding-bottom: 18px;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;text-align: center;">\n<p style="text-align: center;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;"><br>\n<span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="font-size:18px"><strong><span style="color:#000000">Unlimited Game Film</span></strong></span></span></p>\n<p style="text-align: center;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;"><span style="color:#000000"><span style="font-size:16px">Watch and download all of your games.&nbsp;</span></span><br>\n&nbsp;</p>\n<div class="mcnTextContent" style="color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;text-align: center;">\n<div style=" margin-bottom: 5%;">\n<table align="center" style="background: linear-gradient(to right, #3d65b0 , #50b0e3); border-radius:20px;">\n<tbody>\n<tr>\n<td style="color: #FFFFFF;font-size: 16px;font-weight: bold;letter-spacing: -0.5px;padding: 10px 30px;text-align: center;" valign="middle"><a href="https://nextpro.com/subscriptions.html#level" style="color:#FFFFFF; text-decoration:none; font-family: Lato" target="_blank">Subscribe Now</a></td>\n</tr>\n</tbody>\n</table>\n</div>\n</div>\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody>\n</table>'

        unlimited_highlights = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageCardBlock">\n<tbody class="mcnImageCardBlockOuter">\n<tr>\n<td class="mcnImageCardBlockInner" valign="top" style="padding-top:9px; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<table border="0" cellpadding="0" cellspacing="0" class="mcnImageCardRightContentOuter" width="100%">\n<tbody><tr>\n<td align="center" valign="top" class="mcnImageCardRightContentInner" style="padding:0;">\n<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnImageCardRightImageContentContainer" width="282">\n<tbody><tr>\n<td class="mcnImageCardRightImageContentE2E " align="left" valign="top" style="padding-top:0px; padding-right:0; padding-bottom:0px; padding-left:0px;">\n<a href="https://nextpro.com/subscriptions.html#level" title="" class="" target="_blank">\n<img alt="" src="https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/aa48c21b-ee91-4615-9402-d552d57f7df5.png" width="282" style="max-width:1316px;" class="mcnImage">\n</a>\n</td>\n</tr>\n</tbody></table>\n<table class="mcnImageCardRightTextContentContainer" align="right" border="0" cellpadding="0" cellspacing="0" width="264">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-right: 18px;padding-top: 18px;padding-bottom: 18px;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;text-align: center;">\n<p style="text-align: center;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;"><br>\n<span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="font-size:18px"><strong><span style="color:#000000">Unlimited Highlight Reels</span></strong></span></span><br>&nbsp;</p>\n<p style="text-align: center;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;"><span style="color:#000000"><span style="font-size:16px">Any time of year, as many as you need. You pick the plays, and we\'ll create your highlight reels.</span></span><br>&nbsp;</p>\n<div class="mcnTextContent" style="color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;text-align: center;">\n<div style=" margin-bottom: 5%;">\n<table align="center" style="background: linear-gradient(to right, #3d65b0 , #50b0e3); border-radius:20px;">\n<tbody>\n<tr>\n<td align="center" style="color:#FFFFFF; font-size:16px; font-weight:bold; letter-spacing:-.5px; padding-top:10px; padding-right:30px; padding-bottom:10px; padding-left:30px;" valign="middle"><a href="https://nextpro.com/subscriptions.html#level" style="color:#FFFFFF; text-decoration:none; font-family: Lato" target="_blank">Subscribe Now</a></td>\n</tr>\n</tbody>\n</table>\n</div>\n</div>\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody>\n</table>'

        showcase_profile = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageCardBlock">\n<tbody class="mcnImageCardBlockOuter"><tr>\n<td class="mcnImageCardBlockInner" valign="top" style="padding-top:9px; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<table border="0" cellpadding="0" cellspacing="0" class="mcnImageCardLeftContentOuter" width="100%">\n<tbody><tr>\n<td align="center" valign="top" class="mcnImageCardLeftContentInner" style="padding:0;">\n<table align="right" border="0" cellpadding="0" cellspacing="0" class="mcnImageCardLeftImageContentContainer" width="282">\n<tbody><tr>\n<td class="mcnImageCardLeftImageContentE2E " align="left" valign="top" style="padding-top:0px; padding-right:0px; padding-bottom:0px; padding-left:0;">\n<a href="https://nextpro.com/subscriptions.html#level" title="" class="" target="_blank">\n<img alt="" src="https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/2a464067-914a-4690-b652-a3577018d397.png" width="264" style="max-width:650px;" class="mcnImage"></a>\n</td>\n</tr>\n</tbody></table>\n<table class="mcnImageCardLeftTextContentContainer" align="left" border="0" cellpadding="0" cellspacing="0" width="264">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-left: 18px;padding-top: 18px;padding-bottom: 18px;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;text-align: center;">\n<p style="text-align: center;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;"><br>\n<span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="font-size:18px"><strong><span style="color:#000000">Showcase Your Profile</span></strong></span></span></p>\n<p style="text-align: center;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;"><span style="color:#000000"><span style="font-size:16px">Create your profile to share with college coaches &amp; recruiters!&nbsp;</span></span><br>\n&nbsp;</p>\n<div class="mcnTextContent" style="color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;text-align: center;">\n<div style=" margin-bottom: 5%;">\n<table align="center" style="background: linear-gradient(to right, #3d65b0 , #50b0e3); border-radius:20px;">\n<tbody>\n<tr>\n<td style="color: #FFFFFF;font-size: 16px;font-weight: bold;letter-spacing: -0.5px;padding: 10px 30px;text-align: center;" valign="middle"><a href="https://nextpro.com/subscriptions.html#level" style="color:#FFFFFF; text-decoration:none; font-family: Lato" target="_blank">Subscribe Now</a></td>\n</tr>\n</tbody>\n</table>\n</div>\n</div>\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody>\n</table>'

        other_events = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="color:#000000"><strong><span style="font-size:18px">WE FILM OVER 150 EVENTS PER YEAR!</span></strong></span><br>\nincluding events hosted by:</div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCodeBlock">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner">\n<div align="center">\n<img src="' + partner_logo + '" style="width: 40%">\n</div><table>\n</table>\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnBoxedTextBlock" style="min-width:100%;">\n<!--[if gte mso 9]>\n<table align="center" border="0" cellspacing="0" cellpadding="0" width="100%">\n<![endif]-->\n<tbody class="mcnBoxedTextBlockOuter">\n<tr>\n<td valign="top" class="mcnBoxedTextBlockInner">\n<!--[if gte mso 9]>\n<td align="center" valign="top" ">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width:100%;" class="mcnBoxedTextContentContainer">\n<tbody><tr>\n<td style="padding-top:9px; padding-left:18px; padding-bottom:9px; padding-right:18px;">\n<table border="0" cellspacing="0" class="mcnTextContentContainer" width="100%" style="min-width: 100% !important;background-color: #0392D4;">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding: 18px;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;text-align: center;">\n<div style="text-align: center;"><font face="lato, helvetica neue, helvetica, arial, sans-serif"><span style="font-size:16px">You get all of your events that we film included<br>\nfor the year for one low price.</span></font><br>\n(Plus all of 2017)</div>\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody></table>\n<!--[if gte mso 9]>\n</td>\n<![endif]-->\n<!--[if gte mso 9]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><br>\n<span style="font-size:18px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><strong><span style="color:#000000">We\'ve got all of your 2018 events covered.</span></strong></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCodeBlock">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner">\n<div class="mcnTextContent">\n<div style=" margin-bottom: 5%;">\n<table align="center" style="background: linear-gradient(to right, #3d65b0 , #50b0e3); border-radius:20px;">\n<tbody><tr>\n<td align="center" valign="middle" style="color:#FFFFFF; font-size:16px; font-weight:bold; letter-spacing:-.5px; padding-top:10px; padding-right:30px; padding-bottom:10px; padding-left:30px;">\n<a href="https://nextpro.com/lacrosse.txt" target="_blank" style="color:#FFFFFF; text-decoration:none; font-family: Lato">\nView Upcoming Events</a>\n</td>\n</tr>\n</tbody></table>\n</div></div></td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="font-size:18px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><strong><span style="color:#000000">We&nbsp;even&nbsp;got your 2017 events covered too.</span></strong></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCodeBlock">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner">\n<div class="mcnTextContent">\n<div style=" margin-bottom: 5%;">\n<table align="center" style="background: linear-gradient(to right, #3d65b0 , #50b0e3); border-radius:20px;">\n<tbody><tr>\n<td align="center" valign="middle" style="color:#FFFFFF; font-size:16px; font-weight:bold; letter-spacing:-.5px; padding-top:10px; padding-right:30px; padding-bottom:10px; padding-left:30px;">\n<a href="https://nextpro.com/past-events.txt" target="_blank" style="color:#FFFFFF; text-decoration:none;">\nView Past Events</a>\n</td>\n</tr>\n</tbody></table>\n</div></div></td>\n</tr>\n</tbody>\n</table>'

        play_hard = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="font-size:22px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="color:#000000"><strong>Play Hard. Be Visible. Get Recruited.</strong></span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        #Basesball + Softball Email #1 Top section

        baseball_top1 = '<tr>\n<td align="center" valign="top" id="templateBody" data-template-container>\n<!--[if (gte mso 9)|(IE)]>\n<table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">\n<tr>\n<td align="center" valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">\n<tr>\n<td valign="top" class="bodyContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding: 0px 18px 9px; line-height: 200%;">\n<p style="text-align: center; line-height: 200%;"><span style="font-size:30px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><strong><span style="color:#000000">Calling All High Academic Ball Players!</span></strong></span></span><br>\n<span style="font-size:20px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><strong><span style="color:#000000">Get Unlimited&nbsp;Highlight Reels</span></strong></span></span><br>\n<font color="#000000" face="lato, helvetica neue, helvetica, arial, sans-serif"><span style="font-size:20px"><strong>For</strong></span></font><span style="color:#0000FF"><font face="lato, helvetica neue, helvetica, arial, sans-serif"><span style="font-size:20px"><strong> ' + event_name + '</strong></span></font></span></p>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        #EMAIL TEMPLATE 2

        email2_top = "<tr>\n<td align=\"center\" valign=\"top\" id=\"templateBody\" data-template-container>\n<!--[if (gte mso 9)|(IE)]>\n<table align=\"center\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"600\" style=\"width:600px;\">\n<tr>\n<td align=\"center\" valign=\"top\" width=\"600\" style=\"width:600px;\">\n<![endif]-->\n<table align=\"center\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"templateContainer\">\n<tr>\n<td valign=\"top\" class=\"bodyContainer\"><table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnTextBlock\" style=\"min-width:100%;\">\n<tbody class=\"mcnTextBlockOuter\">\n<tr>\n<td valign=\"top\" class=\"mcnTextBlockInner\" style=\"padding-top:9px;\">\n<!--[if mso]>\n<table align=\"left\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\" style=\"width:100%;\">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign=\"top\" width=\"600\" style=\"width:600px;\">\n<![endif]-->\n<table align=\"left\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" style=\"max-width:100%; min-width:100%;\" width=\"100%\" class=\"mcnTextContentContainer\">\n<tbody><tr>\n<td valign=\"top\" class=\"mcnTextContent\" style=\"padding: 0px 18px 9px; line-height: 200%;\">\n<p style=\"text-align: center; line-height: 200%;\"><span style=\"font-size:20px\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\"><strong><span style=\"color:#000000\">Get maximum coverage at</span></strong></span></span><br><font color=\"#000000\" face=\"lato, helvetica neue, helvetica, arial, sans-serif\"><span style=\"font-size:20px\"></span></font><span style=\"color:#0000FF\"><font face=\"lato, helvetica neue, helvetica, arial, sans-serif\"><span style=\"font-size:20px\"><strong> " +  event_name + "</strong></span></font></span></p>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnTextBlock\" style=\"min-width:100%;\">\n<tbody class=\"mcnTextBlockOuter\">\n<tr>\n<td valign=\"top\" class=\"mcnTextBlockInner\" style=\"padding-top:9px;\">\n<!--[if mso]>\n<table align=\"left\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\" style=\"width:100%;\">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign=\"top\" width=\"600\" style=\"width:600px;\">\n<![endif]-->\n<table align=\"left\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" style=\"max-width:100%; min-width:100%;\" width=\"100%\" class=\"mcnTextContentContainer\">\n<tbody><tr>\n<td valign=\"top\" class=\"mcnTextContent\" style=\"padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;\">\n<div style=\"text-align: center;\"><span style=\"font-size:18px\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\"><span style=\"color:#000000\">Score&nbsp;a great deal on u<span style=\"line-height:1.25\">nlimited game film </span>plus</span></span><span style=\"color:#000000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\">&nbsp;h</span>ighlight reels.</span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>"

        unlimited_game_film2 = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="font-size:20px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="color:#000000"><strong>Unlimited Game Film</strong></span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock" style="min-width:100%;">\n<tbody class="mcnImageBlockOuter">\n<tr>\n<td valign="top" style="padding:9px" class="mcnImageBlockInner">\n<table align="left" width="100%" border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="min-width:100%;">\n<tbody><tr>\n<td class="mcnImageContent" valign="top" style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0; text-align:center;">\n<a href="https://nextpro.com/subscriptions.html#level" title="" class="" target="_blank">\n<img align="center" alt="" src="https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/8100fcee-68e7-4b02-9f5b-bc5d4b4e011b.png" width="564" style="max-width:650px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" class="mcnImage">\n</a>\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding: 0px 18px 9px; line-height: 100%;">\n<div style="text-align: center;"><br>\n<br>\n<span style="font-size:18px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="color:#000000"><span style="line-height:1.25">Download&nbsp;your games for 2018 and 2017 now&nbsp;for one low price.</span></span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        discount_with_button = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding: 0px 18px 9px; line-height: 100%;">\n<div style="text-align: center;"><br>\n<br>\n<span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="font-size:18px"><strong><span style="line-height:1.25"><span style="color:#000000">Enter code</span>&nbsp;</span><span style="color:#3d65b0"><span style="line-height:1.25"> '+ discount_code + ' </span></span><span style="color:#000000"><span style="line-height:1.25">&nbsp;at checkout</span></span></strong><br>\n<span style="color:#FF0000; line-height: 1.25;">Expires ' + pre_expiration_date + ' at midnight</span></span></span><br>\n&nbsp;</div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCodeBlock">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner">\n<div class="mcnTextContent">\n<div>\n<table align="center" style="background: linear-gradient(to right, #3d65b0 , #50b0e3); border-radius:60px;">\n<tbody><tr>\n<td align="center" valign="middle" style="color:#FFFFFF; font-size:24px; font-weight:bold; letter-spacing:-.5px; padding-top:20px; padding-right:60px; padding-bottom:20px; padding-left:60px;">\n<a href="https://nextpro.com/subscriptions.html#level" target="_blank" style="color:#FFFFFF; text-decoration:none; font-family: Lato">Subscribe Now</a>\n</td>\n</tr>\n</tbody></table>\n</div>\n</div>\n</td>\n</tr>\n</tbody>\n</table>'

        unlimited_highlights2 = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="font-size:20px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="color:#000000"><strong>Unlimited Highlight Reels</strong></span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock" style="min-width:100%;">\n<tbody class="mcnImageBlockOuter">\n<tr>\n<td valign="top" style="padding:9px" class="mcnImageBlockInner">\n<table align="left" width="100%" border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="min-width:100%;">\n<tbody><tr>\n<td class="mcnImageContent" valign="top" style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0; text-align:center;">\n<a href="https://nextpro.com/subscriptions.html#level" title="" class="" target="_blank">\n<img align="center" alt="" src="https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/aa48c21b-ee91-4615-9402-d552d57f7df5.png" width="564" style="max-width:650px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" class="mcnImage">\n</a>\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding: 0px 18px 9px; line-height: 100%;">\n<div style="text-align: center;"><br><span style="font-size:18px"><span style="color:#000000"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif">Whether you need one highlight reel or ten,&nbsp;</span></span></span><br>\n<span style="font-size:18px"><span style="color:#000000"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif; line-height:1.25">you pick the plays, we do the editing.</span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        #EMAIL TEMPLATE 3

        email3_top = '<tr>\n<td align="center" valign="top" id="templateBody" data-template-container>\n<!--[if (gte mso 9)|(IE)]>\n<table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">\n<tr>\n<td align="center" valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">\n<tr>\n<td valign="top" class="bodyContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;"> \n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding: 0px 18px 9px; line-height: 150%;">\n<div style="text-align: center;"><br>\n<span style="font-size:20px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="color:#000000"><strong>Only 48 HOURS Left!</strong> </span></span></span><br>\n<span style="font-size:18px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="color:#000000">Get&nbsp;our&nbsp;Pre-Event Discount on Game Film and Highlight Reels for</span><br>\n<span style="color:#0000FF"> ' + event_name + ' </span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        pre_event_timer_block = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;">' + pre_event_timer + '</div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        shareable_profile3 = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="color:#000000"><strong><span style="font-size:18px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif">Shareable Player Profile</span></span></strong></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock" style="min-width:100%;">\n<tbody class="mcnImageBlockOuter">\n<tr>\n<td valign="top" style="padding:9px" class="mcnImageBlockInner">\n<table align="left" width="100%" border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="min-width:100%;">\n<tbody><tr>\n<td class="mcnImageContent" valign="top" style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0; text-align:center;">\n<img align="center" alt="" src="https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/ba01f625-b3c9-455d-8ec6-b0e8bc65d928.png" width="564" style="max-width:650px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" class="mcnImage">\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnDividerBlock" style="min-width:100%;">\n<tbody class="mcnDividerBlockOuter">\n<tr>\n<td class="mcnDividerBlockInner" style="min-width:100%; padding:18px;">\n<table class="mcnDividerContent" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width: 100%;border-top: 2px none #EAEAEA;">\n<tbody><tr>\n<td>\n<span></span>\n</td>\n</tr>\n</tbody></table>\n<!--\n<td class="mcnDividerBlockInner" style="padding: 18px;">\n<hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />\n-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCodeBlock">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner">\n<div class="mcnTextContent">\n<div>\n<table align="center" style="background: linear-gradient(to right, #3d65b0 , #50b0e3); border-radius:60px;">\n<tbody><tr>\n<td align="center" valign="middle" style="color:#FFFFFF; font-size:24px; font-weight:bold; letter-spacing:-.5px; padding-top:20px; padding-right:60px; padding-bottom:20px; padding-left:60px;">\n<a href="https://nextpro.com/subscriptions.html#level" target="_blank" style="color:#FFFFFF; text-decoration:none; font-family: Lato">Subscribe Now</a>\n</td>\n</tr>\n</tbody></table>\n</div>\n</div></td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding: 0px 18px 9px; line-height: 125%;">\n<div style="text-align: center;"><br>\n<span style="font-size:18px"><span style="color:#000000"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif">Share your highlight reels with college coaches and recruiters<br>\nwith our free player profiles!</span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        #EMAIL TEMPLATE 4

        email4_top = '<tr>\n<td align="center" valign="top" id="templateBody" data-template-container>\n<!--[if (gte mso 9)|(IE)]>\n<table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">\n<tr>\n<td align="center" valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">\n<tr>\n<td valign="top" class="bodyContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;"> \n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding: 0px 18px 9px; line-height: 150%;">\n<div style="text-align: center;"><br>\n<span style="font-size:20px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="color:#000000"><strong>Only 24 HOURS Left!</strong> </span></span></span><br>\n<span style="font-size:18px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="color:#000000">Get&nbsp;our&nbsp;Pre-Event Discount on Game Film and Highlight Reels for</span><br>\n<span style="color:#0000FF"> ' + event_name + ' </span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        #baseball + softball email 4 top
        email4_top_basesoft = '<tr>\n<td align="center" valign="top" id="templateBody" data-template-container>\n<!--[if (gte mso 9)|(IE)]>\n<table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">\n<tr>\n<td align="center" valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">\n<tr>\n<td valign="top" class="bodyContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding: 0px 18px 9px; line-height: 150%;">\n<div style="text-align: center;"><br>\n<span style="font-size:20px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="color:#000000"><strong>Only 24 HOURS Left!</strong> </span></span></span><br>\n<span style="font-size:18px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="color:#000000">Hey Batters and Pitchers,<br>\nGet&nbsp;our&nbsp;Pre-Event Discount on Player Clips and Highlight Reels for</span><br>\n<span style="color:#0000FF">' + event_name + '</span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;">' + pre_event_timer + '</div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCodeBlock">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner">\n<div class="mcnTextContent">\n<div>\n<table align="center" style="background: linear-gradient(to right, #3d65b0 , #50b0e3); border-radius:60px;">\n<tbody><tr>\n<td align="center" valign="middle" style="color:#FFFFFF; font-size:18px; font-weight:bold; letter-spacing:-.5px; padding-top:20px; padding-right:60px; padding-bottom:20px; padding-left:60px;">\n<a href="https://nextpro.com/subscriptions.html#level" target="_blank" style="color:#FFFFFF; text-decoration:none; font-family: Lato">Subscribe Now</a>\n</td>\n</tr>\n</tbody></table>\n</div>\n</div>\n</td>\n</tr>\n</tbody>\n</table>'

        #EMAIL TEMPLATE 5a

        email5a_top = '<tr>\n<td align="center" valign="top" id="templateBody" data-template-container>\n<!--[if (gte mso 9)|(IE)]>\n<table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">\n<tr>\n<td align="center" valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">\n<tr>\n<td valign="top" class="bodyContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="font-size:24px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif; line-height:1.25"><font color="#000000"><strong>NextPro is&nbsp;at </strong></font><span style="color:#0000FF"><strong>' + event_name + '</strong></span><font color="#000000"><strong>!</strong></font></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        booth_section = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding: 0px 18px 9px; line-height: 150%;">\n<div style="text-align: center;"><span style="font-size:22px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif; line-height:1.25"><font color="#000000"><strong>Stop By Our Booth Today For More Savings</strong></font></span></span><br>\n<span style="font-size:20px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif; line-height:1.25"><font color="#000000">Get Unlimited Game Film Downloads and Highlight&nbsp;Reels</font></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock" style="min-width:100%;">\n<tbody class="mcnImageBlockOuter">\n<tr>\n<td valign="top" style="padding:9px" class="mcnImageBlockInner">\n<table align="left" width="100%" border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="min-width:100%;">\n<tbody><tr>\n<td class="mcnImageContent" valign="top" style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0; text-align:center;">\n<a href="https://nextpro.com/subscriptions.html" title="" class="" target="_blank">\n<img align="center" alt="" src="https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/54b9a433-d10c-49eb-8ce7-39620cd1e118.jpg" width="564" style="max-width:600px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" class="mcnImage">\n</a>\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="color:#000000"><span style="font-size:18px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif">Speak with our team to receive event day only discounts</span><br>\nand also be entered into our drawing for free subscriptions and prizes</span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        get_player_profile = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="font-size:20px"><strong><span style="color:#000000"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif">Get Your Player Profile</span></span></strong></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock" style="min-width:100%;">\n<tbody class="mcnImageBlockOuter">\n<tr>\n<td valign="top" style="padding:9px" class="mcnImageBlockInner">\n<table align="left" width="100%" border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="min-width:100%;">\n<tbody><tr>\n<td class="mcnImageContent" valign="top" style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0; text-align:center;">\n<img align="center" alt="" src="https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/ba01f625-b3c9-455d-8ec6-b0e8bc65d928.png" width="564" style="max-width:650px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" class="mcnImage">\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="font-size:18px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><font color="#000000">Need help building a player profile?&nbsp;<br>\nOur on site team is here to help get you setup.&nbsp;</font></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        #EMAIL TEMPLATE 5

        email5_top = '<tr>\n<td align="center" valign="top" id="templateBody" data-template-container>\n<!--[if (gte mso 9)|(IE)]>\n<table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">\n<tr>\n<td align="center" valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">\n<tr>\n<td valign="top" class="bodyContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="font-size:20px"><strong><span style="color:#0000FF"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif">' + event_name + ' </span></span><span style="color:#000000"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"> Starts Today!</span></span></strong></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        #EMAIL TEMPLATE 6b

        email6_top = '<tr>\n<td align="center" valign="top" id="templateBody" data-template-container>\n<!--[if (gte mso 9)|(IE)]>\n<table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">\n<tr>\n<td align="center" valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">\n<tr>\n<td valign="top" class="bodyContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><strong><span style="font-size:36px"><span style="color:#000000; line-height:1.25">How Did You Play at<br>\n' + event_name + '?</span></span></strong></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div dir="ltr" style="text-align: center;"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="color:#000000"><span style="font-size:26px">There\'s still time to order film!</span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        email6_top_basesoft = '<tr>\n<td align="center" valign="top" id="templateBody" data-template-container>\n<!--[if (gte mso 9)|(IE)]>\n<table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">\n<tr>\n<td align="center" valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">\n<tr>\n<td valign="top" class="bodyContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><strong><span style="font-size:36px"><span style="color:#000000; line-height:1.25">How Did You Play at<br>\n' + event_name + '?</span></span></strong></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div dir="ltr" style="text-align: center;"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="color:#000000"><span style="font-size:26px">There\'s still time to order highlight reels!</span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        dark_timer_coupon_lax = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCodeBlock">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner">\n<div class="mcnTextContent">\n<div align="center" style="background: #000; padding-top: 15px; padding-bottom: 30px;">\n<a href="https://nextpro.com/subscriptions.html#level" target="_blank"><img src="https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/21bbd825-d090-4f41-8799-ffb9a021235e.png" style="width: 40%; padding:2%" alt="Logo"></a>\n<h1 style="color:#fff; font-family: Lato; text-align: center;font-size: 42pt">Game Film + Highlights</h1>\n' + post_event_timer_black_background + '\n<p style="color:#fff; font-family: Lato; text-align: center; font-size: 28pt">Use code <span style="color:#ff2a03">' + post_event_promo_code + '</span> for 10% off.</p>\n<table>\n<tbody>\n<tr>\n<td align="center" style="width: 200px; height: 45px; background: #28a9ff; border-radius: 5px">\n<a href="https://nextpro.com/subscriptions.html#level" style="color: #fff; text-decoration: none; font-family: Lato; font-size: 18pt;" target="_blank">Subscribe Now</a>\n</td>\n</tr>\n</tbody>\n</table><table>\n</table></div></div></td></tr></tbody></table>'

        dark_timer_coupon_basesoft = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCodeBlock">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner">\n<div class="mcnTextContent">\n<div align="center" style="background: #000; padding-top: 15px; padding-bottom: 30px;">\n<a href="https://nextpro.com/subscriptions.html#level" target="_blank"><img src="https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/21bbd825-d090-4f41-8799-ffb9a021235e.png" style="width: 40%; padding:2%" alt="Logo"></a>\n<h1 style="color:#fff; font-family: Lato; text-align: center;font-size: 42pt">Got Highlight Reels?</h1>\n' + post_event_timer_black_background + '\n<p style="color:#fff; font-family: Lato; text-align: center; font-size: 28pt">Use code <span style="color:#ff2a03">' + post_event_promo_code + '</span> for $100 off.</p>\n<table>\n<tbody>\n<tr>\n<td align="center" style="width: 200px; height: 45px; background: #28a9ff; border-radius: 5px">\n<a href="https://nextpro.com/subscriptions.html#level" style="color: #fff; text-decoration: none; font-family: Lato; font-size: 18pt;" target="_blank">Subscribe Now</a>\n</td>\n</tr>\n</tbody>\n</table><table>\n</table></div></div></td></tr></tbody></table>'

        caveat2 = "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnTextBlock\" style=\"min-width:100%;\">\n<tbody class=\"mcnTextBlockOuter\">\n<tr>\n<td valign=\"top\" class=\"mcnTextBlockInner\" style=\"padding-top:9px;\">\n<!--[if mso]>\n<table align=\"left\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\" style=\"width:100%;\">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign=\"top\" width=\"600\" style=\"width:600px;\">\n<![endif]-->\n<table align=\"left\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" style=\"max-width:100%; min-width:100%;\" width=\"100%\" class=\"mcnTextContentContainer\">\n<tbody><tr>\n<td valign=\"top\" class=\"mcnTextContent\" style=\"padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;\">\n<div style=\"text-align: center;\"><span style=\"font-size:20px\"><span style=\"color:#000000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif; line-height:1.25\">Use code</span></span><span style=\"color:#FF0000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\"> </span></span><span style=\"color:#3d65b0\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\">" + post_event_promo_code + " </span></span><span style=\"color:#FF0000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\"> </span></span><span style=\"color:#000000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\">at checkout</span></span></span><br>\n<span style=\"font-size:18px\"><span style=\"color:#FF0000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\">Expires " + post_code_expiration + " at midnight</span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>"

        caveat3 = "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnTextBlock\" style=\"min-width:100%;\">\n<tbody class=\"mcnTextBlockOuter\">\n<tr>\n<td valign=\"top\" class=\"mcnTextBlockInner\" style=\"padding-top:9px;\">\n<!--[if mso]>\n<table align=\"left\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"100%\" style=\"width:100%;\">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign=\"top\" width=\"600\" style=\"width:600px;\">\n<![endif]-->\n<table align=\"left\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" style=\"max-width:100%; min-width:100%;\" width=\"100%\" class=\"mcnTextContentContainer\">\n<tbody><tr>\n<td valign=\"top\" class=\"mcnTextContent\" style=\"padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;\">\n<div style=\"text-align: center;\"><span style=\"font-size:20px\"><span style=\"color:#000000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif; line-height:1.25\">Use code</span></span><span style=\"color:#FF0000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\"> </span></span><span style=\"color:#3d65b0\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\">" + post_event_promo_code + " </span></span><span style=\"color:#FF0000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\"> </span></span><span style=\"color:#000000\"><span style=\"font-family:lato,helvetica neue,helvetica,arial,sans-serif\">at checkout</span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>"

        estimated_date = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><br>\n<span style="color:#000000; line-height:1.25"><span style="font-size:18px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><strong>Your game film is estimated to be delivered&nbsp;by </strong></span></span></span><strong><span style="color:#3d65b0"><span style="line-height:1.25"><span style="font-size:18px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif">' + estimated_delivery + '</span></span></span></span></strong></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        #TEXT ONLY TEMPLATE - CURRENTLY EMAIL #7

        text_only_body = '<tr>\n<td valign="top" id="templateBody"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\nThe competition was fierce at ' + event_name + '!&nbsp; And we caught all the action.<br>\n<br>\nReview your performance on the field with unlimited access to your NextPro game film.&nbsp; Increase your recruiting opportunities with our professionally edited highlight reels. Nextpro Highlight reels showcase your best plays for college coaches and recruiting professionals.&nbsp;&nbsp;<br>\n&nbsp;\n<div style="text-align: left;">Order today and get an extra 10% off. Use code <span style="color:#3d65b0">' + post_event_promo_code + '</span> at checkout.&nbsp;<a href="https://nextpro.com/signup" target="_blank"><span style="color:#3d65b0">Click here to order now.</span></a><br>\n<br>\nSee you at the next game!</div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock" style="min-width:100%;">\n<tbody class="mcnImageBlockOuter">\n<tr>\n<td valign="top" style="padding:9px" class="mcnImageBlockInner">\n<table align="left" width="100%" border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="min-width:100%;">\n<tbody><tr>\n<td class="mcnImageContent" valign="top" style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0;">\n<a href="https://nextpro.com/subscriptions.html" title="" class="" target="_blank">\n<img align="left" alt="" src="https://gallery.mailchimp.com/544d3bd85dbfc6be22720dd7f/images/3c1e5794-2133-4c10-b0cc-33ec3b4ae697.png" width="135" style="max-width:270px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" class="mcnRetinaImage">\n</a>\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody>\n</table>'

        #EMAIL 7 Template - NOW EMAIL #8

        video_block = '<!--****** VIDEO BLOCK *****-->\n<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageCardBlock">\n<tbody class="mcnImageCardBlockOuter">\n<tr>\n<td class="mcnImageCardBlockInner" valign="top" style="padding-top:9px; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnImageCardBottomContent" width="100%" style="background-color: #404040;">\n<tbody><tr>\n<td class="mcnImageCardBottomImageContent" align="center" valign="top" style="padding-top:0px; padding-right:0px; padding-bottom:0; padding-left:0px;">\n<a href="' + video_link + '" title="" class="" target="">\n<img alt="" src="' + video_alt_img + '" width="564" style="max-width:1922px;" class="mcnImage">\n</a>\n</td>\n</tr>\n<tr>\n<td class="mcnTextContent" valign="top" style="padding: 9px 18px;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;text-align: center;" width="546">\n' + video_title + '\n</td>\n</tr>\n</tbody></table>\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCodeBlock">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner">\n<div class="mcnTextContent">\n<div style="margin-top:5%; margin-bottom: 5%;">\n<table align="center" style="background: linear-gradient(to right, #3d65b0 , #50b0e3); border-radius:20px;">\n<tbody><tr>\n<td align="center" valign="middle" style="color:#FFFFFF; font-size:16px; font-weight:bold; letter-spacing:-.5px; padding-top:10px; padding-right:30px; padding-bottom:10px; padding-left:30px;">\n<a href="https://nextpro.com/subscriptions.html" target="_blank" style="color:#FFFFFF; text-decoration:none;">\nGet Your Highlights</a>\n</td>\n</tr>\n</tbody></table>\n</div>\n</div>\n</td>\n</tr>\n</tbody>\n</table>'

        email7_timer = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="font-size:30px"><span style="color:#FF0000"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="line-height:1.25">Get 10% off your order</span></span></span></span></div>\n<div style="text-align: center;"><span style="font-size:30px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="line-height:1.25"><span style="color:#000000">Use code </span><span style="color:#3d65b0">' + post_event_promo_code + '</span><span style="color:#000000"> at checkout.</span></span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><br>'

        email7_timer_basesoft = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n' + post_event_timer1 + '\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\n<div style="text-align: center;"><span style="font-size:30px"><span style="color:#FF0000"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="line-height:1.25">Get $100 off your order</span></span></span></span></div>\n<div style="text-align: center;"><span style="font-size:30px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"><span style="line-height:1.25"><span style="color:#000000">Use code </span><span style="color:#3d65b0">' + post_event_promo_code + '</span><span style="color:#000000"> at checkout.</span></span></span></span></div>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        #Email 6a Template

        # $50 off coupon
        lacrosse6a_coupon = "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" class=\"mcnCodeBlock\">\n<tbody class=\"mcnTextBlockOuter\">\n<tr>\n<td valign=\"top\" class=\"mcnTextBlockInner\">\n<div class=\"mcnTextContent\"><div align=\"center\" style=\"background: #000; padding-top: 15px; padding-bottom: 30px;\">\n<a href=\"https://nextpro.com/subscriptions.html#level\" target=\"_blank\"><img src=\"https://gallery.mailchimp.com/7d973963555bfe9adf1b01a82/images/21bbd825-d090-4f41-8799-ffb9a021235e.png\" style=\"width: 40%; padding:2%\" alt=\"Logo\"></a>\n<h1 style=\"color:#fff; font-family: Lato; text-align: center;font-size: 42pt\">Game Film + Highlights</h1><p style=\"color:#fff; font-family: Lato; text-align: center; font-size: 28pt\">Use code <span style=\"color:#ff2a03\">" + coupon_code6a + "</span> for $50 off.</p>\n<table>\n<tbody>\n<tr>\n<td align=\"center\" style=\"width: 200px; height: 45px; background: #28a9ff; border-radius: 5px\">\n<a href=\"https://nextpro.com/subscriptions.html#level\" style=\"color: #fff; text-decoration: none; font-family: Lato; font-size: 18pt;\" target=\"_blank\">Subscribe Now</a>\n</td>\n</tr>\n</tbody>\n</table><table>\n</table></div></div></td></tr></tbody></table>"

        #Email 3a

        lacrosse3a_top = '<tr>\n<td align="center" valign="top" id="templateBody" data-template-container>\n<!--[if (gte mso 9)|(IE)]>\n<table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">\n<tr>\n<td align="center" valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">\n<tr>\n<td valign="top" class="bodyContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\n<!--[if mso]>\n<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\n<tr>\n<![endif]-->\n<!--[if mso]>\n<td valign="top" width="600" style="width:600px;">\n<![endif]-->\n<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\n<tbody><tr>\n<td valign="top" class="mcnTextContent" style="padding: 0px 18px 9px; line-height: 200%;">\n<p style="text-align: center; line-height: 200%;"><font color="#000000" face="lato, helvetica neue, helvetica, arial, sans-serif"><span style="font-size:20px"><strong>We\'re glad&nbsp;you&nbsp;registered&nbsp;</strong></span></font><br>\n<font color="#000000" face="lato, helvetica neue, helvetica, arial, sans-serif"><span style="font-size:20px"><strong>for</strong></span></font><span style="color:#0000FF"><font face="lato, helvetica neue, helvetica, arial, sans-serif"><span style="font-size:20px"><strong> ' + event_name + '</strong></span></font></span><br>\n<strong><span style="color:#000000"><span style="font-size:20px"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif">Don\'t Miss Last Minute Savings on Unlimited Highlight Reels!</span></span></span></strong></p>\n</td>\n</tr>\n</tbody></table>\n<!--[if mso]>\n</td>\n<![endif]-->\n<!--[if mso]>\n</tr>\n</table>\n<![endif]-->\n</td>\n</tr>\n</tbody>\n</table>'

        #Email 6 Template

        save_10 = '<table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCodeBlock">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner">\n<div class="mcnTextContent"><br><br>\n<div>\n<table align="center" style="background: linear-gradient(to right, #3d65b0 , #50b0e3); border-radius:60px;">\n<tbody><tr>\n<td align="center" valign="middle" style="color:#FFFFFF; font-size:24px; font-weight:bold; letter-spacing:-.5px; padding-top:20px; padding-right:60px; padding-bottom:20px; padding-left:60px;">\n<a href="https://nextpro.com/subscriptions.html#level" target="_blank" style="color:#FFFFFF; text-decoration:none; font-family: Lato">Subscribe Now</a>\n</td>\n</tr>\n</tbody></table>\n</div>\n</div>\n</td>\n</tr>\n</tbody>\n</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCodeBlock">\n<tbody class="mcnTextBlockOuter">\n<tr>\n<td valign="top" class="mcnTextBlockInner">\n<div style="text-align: center;"><br>\n<span style="font-size:16px"><span style="color:#000000"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif">Save 15%. Use code </span></span><span style="color:#0000FF"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif">' + post_event_promo_code + '</span></span><span style="color:#000000"><span style="font-family:lato,helvetica neue,helvetica,arial,sans-serif"> at checkout.</span></span></span></div>\n</td>\n</tr>\n</tbody>\n</table>'




        #ADD CONTENT TO HTML DOCUMENTS

        #LACROSSE TEMPLATES

        if(sport_selection == "Lacrosse"):
            #add header content to all files
            with open("initialize.txt") as f:
                with open("emails/lacrosse1a.txt", "w") as f1a:
                    for line in f:
                        f1a.write(line)
                f1a.close()
                f.seek(0, 0)
                with open("emails/lacrosse1.txt", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/lacrosse2.txt", "w") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/lacrosse3a.txt", "w") as f3a:
                    for line in f:
                         f3a.write(line)
                f3a.close()
                f.seek(0, 0)
                with open("emails/lacrosse3.txt", "w") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/lacrosse4.txt", "w") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/lacrosse5a.txt", "w") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/lacrosse5.txt", "w") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/lacrosse6b.txt", "w") as f6b:
                    for line in f:
                         f6b.write(line)
                f6b.close()
                f.seek(0, 0)
                with open("emails/lacrosse6a.txt", "w") as f6a:
                    for line in f:
                        f6a.write(line)
                f6a.close()
            f.close()

            with open("lacrosse-template-parts/email6-new-init.txt") as f:
                with open("emails/lacrosse6.txt", "w") as f6:
                    for line in f:
                        f6.write(line)
                f6.close()
            f.close()

            with open("textonly-init.txt") as f:
                with open("emails/lacrosse7.txt", "w") as f7:
                    for line in f:
                        f7.write(line)
                f7.close()
            f.close()


            with open("initialize7.txt") as f:
                with open("emails/lacrosse8.txt", "w") as f8:
                    for line in f:
                         f8.write(line)
                f8.close()
            f.close()

            #add header
            with open("header.txt") as f:
                with open("emails/lacrosse1a.txt", "a+") as f1a:
                    for line in f:
                        f1a.write(line)
                f1a.close()
                f.seek(0, 0)
                with open("emails/lacrosse1.txt", "a+") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/lacrosse2.txt", "a+") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/lacrosse3a.txt", "a+") as f3a:
                    for line in f:
                         f3a.write(line)
                f3a.close()
                f.seek(0, 0)
                with open("emails/lacrosse3.txt", "a+") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/lacrosse4.txt", "a+") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/lacrosse5a.txt", "a+") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/lacrosse5.txt", "a+") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/lacrosse6b.txt", "a+") as f6b:
                    for line in f:
                         f6b.write(line)
                f6b.close()
                f.seek(0, 0)
                with open("emails/lacrosse8.txt", "a+") as f8:
                    for line in f:
                         f8.write(line)
                f8.close()
                f.seek(0, 0)
                with open("emails/lacrosse6a.txt", "a+") as f6a:
                    for line in f:
                        f6a.write(line)
                f6a.close()
            f.close()

            #Lacrosse Body

            with open("emails/lacrosse1a.txt", "a+") as file1a:
                file1a.write(finish_header)
                file1a.write(email1a_top)
                file1a.write(divider)
                #file1a.write(email1a_timer_coupon)
                file1a.write(caveat)
                file1a.write(divider)
                file1a.write(unlimited_game_film)
                file1a.write(divider)
                file1a.write(unlimited_highlights)
                file1a.write(divider)
                file1a.write(showcase_profile)
                file1a.write(divider)
                file1a.write(other_events)
                file1a.write(divider)
                file1a.write(play_hard)
                file1a.write(divider)
                file1a.write(email1a_testimonials)
                file1a.close()
            with open("emails/lacrosse1.txt", "a+") as file:
                file.write(finish_header)
                file.write(email1_section1)
                file.write(coupon_lacrosse)
                file.write(caveat)
                file.write(divider)
                file.write(unlimited_game_film)
                file.write(divider)
                file.write(unlimited_highlights)
                file.write(divider)
                file.write(showcase_profile)
                file.write(divider)
                file.write(other_events)
                file.write(divider)
                file.write(play_hard)
                file.write(divider)
                file.close()
            with open("emails/lacrosse2.txt", "a+") as file2:
                file2.write(finish_header)
                file2.write(email2_top)
                file2.write(divider)
                file2.write(unlimited_game_film2)
                file2.write(discount_with_button)
                file2.write(divider)
                file2.write(unlimited_highlights2)
                file2.write(discount_with_button)
                file2.write(divider)
                file2.write(other_events)
                file2.write(divider)
                file2.write(play_hard)
                file2.write(divider)
                file2.close()
            with open("emails/lacrosse3.txt", "a+") as file3:
                file3.write(finish_header)
                file3.write(email3_top)
                file3.write(divider)
                file3.write(pre_event_timer_block)
                file3.write(discount_with_button)
                file3.write(divider)
                file3.write(coupon_lacrosse)
                file3.write(caveat)
                file3.write(divider)
                file3.write(unlimited_highlights)
                file3.write(divider)
                file3.write(shareable_profile3)
                file3.write(divider)
                file3.write(play_hard)
                file3.write(divider)
                file3.close()
            with open("emails/lacrosse4.txt", "a+") as file4:
                file4.write(finish_header)
                file4.write(email4_top)
                file4.write(pre_event_timer_block)
                file4.write(discount_with_button)
                file4.write(divider)
                file4.write(coupon_lacrosse)
                file4.write(caveat)
                file4.write(divider)
                file4.write(unlimited_highlights)
                file4.write(divider)
                file4.write(shareable_profile3)
                file4.write(divider)
                file4.write(play_hard)
                file4.write(divider)
                file4.close()
            with open("emails/lacrosse5a.txt", "a+") as file5a:
                file5a.write(finish_header)
                file5a.write(email5a_top)
                file5a.write(divider)
                file5a.write(booth_section)
                file5a.write(divider)
                file5a.write(get_player_profile)
                file5a.write(divider)
                with open("no_time.txt") as a1:
                    for line in a1:
                        file5a.write(line)
                a1.close()
                file5a.write(divider)
                file5a.close()
            with open("emails/lacrosse5.txt", "a+") as file5:
                file5.write(finish_header)
                file5.write(email5_top)
                file5.write(divider)
                with open("email5-1.txt") as a1:
                    for line in a1:
                        file5.write(line)
                a1.close()
                file5.write(caveat3)
                file5.write(divider)
                with open("enjoy_game.txt") as a2:
                    for line in a2:
                        file5.write(line)
                a2.close()
                file5.write(caveat3)
                file5.write(divider)
                with open("recruiting_tool.txt") as a3:
                    for line in a3:
                        file5.write(line)
                a3.close()
                file5.write(caveat3)
                file5.write(divider)
                file5.write(play_hard)
                file5.write(post_event_coupon_lacrosse)
                file5.close()
            with open("emails/lacrosse6b.txt", "a+") as file6b:
                file6b.write(finish_header)
                file6b.write(email6_top)
                file6b.write(dark_timer_coupon_lax)
                file6b.write(caveat2)
                file6b.write(divider)
                file6b.write(estimated_date)
                with open("email6_middle.txt") as a1:
                    for line in a1:
                        file6b.write(line)
                a1.close()
                file6b.write(divider)
                file6b.write(other_events)
                file6b.write(divider)
                file6b.write(play_hard)
                file6b.write(divider)
                file6b.close()
            with open("emails/lacrosse7.txt", "a+") as file7:
                file7.write(text_only_body)
                file7.write(divider)
                file7.close()
            with open("emails/lacrosse8.txt", "a+") as file8:
                file8.write(finish_header)
                with open("email7_top.txt") as a1:
                    for line in a1:
                        file8.write(line)
                a1.close()
                file8.write(video_block)
                file8.write(divider)
                file8.write(email7_timer)
                file8.write(divider)
                with open("email7_product.txt") as a1:
                    for line in a1:
                        file8.write(line)
                a1.close()
                file8.write(divider)
                with open("testimonials.txt") as a2:
                    for line in a2:
                        file8.write(line)
                a2.close()
                file8.write(divider)
                file8.write(play_hard)
                file8.write(divider)
                file8.close()
            with open("emails/lacrosse6a.txt", "a+") as file6a:
                file6a.write(finish_header)
                with open("lacrosse-template-parts/lax-email6a-body.txt") as a1:
                    for line in a1:
                        file6a.write(line)
                a1.close()
                file6a.write(lacrosse6a_coupon)
                file6a.write(divider)
                file6a.write(play_hard)
                file6a.write(divider)
                file6a.close()
            with open("emails/lacrosse3a.txt", "a+") as file3a:
                file3a.write(finish_header)
                file3a.write(lacrosse3a_top)
                file3a.write(divider)
                file3a.write(pre_event_timer_block)
                file3a.write(discount_with_button)
                file3a.write(divider)
                file3a.write(unlimited_game_film)
                file3a.write(divider)
                file3a.write(unlimited_highlights)
                file3a.write(divider)
                file3a.write(showcase_profile)
                file3a.write(divider)
                file3a.write(other_events)
                file3a.write(divider)
                file3a.write(play_hard)
                file3a.write(divider)
                file3a.write(email1a_testimonials)
                file3a.close()
            with open("emails/lacrosse6.txt", "a+") as file6:
                file6.write(estimated_date)
                file6.write(save_10)
                with open("lacrosse-template-parts/lax6-new-body.txt") as a1:
                    for line in a1:
                        file6.write(line)
                a1.close()
                file6.write(save_10)
                file6.write(divider)
                with open("lacrosse-template-parts/lax6-new-bottom.txt") as a2:
                    for line in a2:
                        file6.write(line)
                a2.close()
                file6.write(divider)
                file6.close()

            #add closing content to all files
            with open("close.txt") as f:
                with open("emails/lacrosse1a.txt", "a+") as f1a:
                    for line in f:
                        f1a.write(line)
                f1a.close()
                f.seek(0, 0)
                with open("emails/lacrosse1.txt", "a+") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/lacrosse2.txt", "a+") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/lacrosse3.txt", "a+") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/lacrosse4.txt", "a+") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/lacrosse5a.txt", "a+") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/lacrosse5.txt", "a+") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/lacrosse6b.txt", "a+") as f6b:
                    for line in f:
                         f6b.write(line)
                f6b.close()
                f.seek(0, 0)
                with open("emails/lacrosse8.txt", "a+") as f8:
                    for line in f:
                         f8.write(line)
                f8.close()
                f.seek(0, 0)
                with open("emails/lacrosse6a.txt", "a+") as f6a:
                    for line in f:
                         f6a.write(line)
                f6a.close()
                f.seek(0, 0)
                with open("emails/lacrosse3a.txt", "a+") as f3a:
                    for line in f:
                         f3a.write(line)
                f3a.close()
                f.seek(0, 0)
                with open("emails/lacrosse6.txt", "a+") as f6:
                    for line in f:
                        f6.write(line)
                f6.close()
            f.close()

            #close text only templates
            with open("close-textonly.txt") as f:
                with open("emails/lacrosse7.txt", "a+") as f7:
                    for line in f:
                        f7.write(line)
                f7.close()
            f.close()


            #Create Preview Templates Lacrosse

            with open("emails/lacrosse1a.txt") as f:
                with open("templates/lacrosse1a.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/lacrosse1.txt") as f:
                with open("templates/lacrosse1.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/lacrosse2.txt") as f:
                with open("templates/lacrosse2.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/lacrosse3.txt") as f:
                with open("templates/lacrosse3.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/lacrosse4.txt") as f:
                with open("templates/lacrosse4.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/lacrosse5a.txt") as f:
                with open("templates/lacrosse5a.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/lacrosse5.txt") as f:
                with open("templates/lacrosse5.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/lacrosse6b.txt") as f:
                with open("templates/lacrosse6b.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/lacrosse7.txt") as f:
                with open("templates/lacrosse7.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/lacrosse8.txt") as f:
                with open("templates/lacrosse8.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/lacrosse6a.txt") as f:
                with open("templates/lacrosse6a.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/lacrosse3a.txt") as f:
                with open("templates/lacrosse3a.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/lacrosse6.txt") as f:
                with open("templates/lacrosse6.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()



        #SOCCER TEMPLATES

        if(sport_selection == "Soccer"):

            #add header content to all files
            with open("initialize.txt") as f:
                with open("emails/soccer1.txt", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/soccer2.txt", "w") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/soccer3.txt", "w") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/soccer4.txt", "w") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/soccer5a.txt", "w") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/soccer5.txt", "w") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/soccer6.txt", "w") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
            f.close()

            with open("initialize7.txt") as f:
                with open("emails/soccer7.txt", "w") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()

            #add header
            with open("header.txt") as f:
                with open("emails/soccer1.txt", "a+") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/soccer2.txt", "a+") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/soccer3.txt", "a+") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/soccer4.txt", "a+") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/soccer5a.txt", "a+") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/soccer5.txt", "a+") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/soccer6.txt", "a+") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
                f.seek(0, 0)
                with open("emails/soccer7.txt", "a+") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()
            f.close()

            #Soccer body

            with open("emails/soccer1.txt", "a+") as file:
                file.write(finish_header)
                file.write(email1_section1)
                file.write(coupon1_soccer)
                file.write(caveat)
                file.write(divider)
                with open("soccer-template-parts/soccer1-body.txt") as a1:
                    for line in a1:
                        file.write(line)
                a1.close()
                file.write(divider)
                file.write(play_hard)
                file.write(divider)
                file.close()
            with open("emails/soccer2.txt", "a+") as file2:
                file2.write(finish_header)
                with open("soccer-template-parts/email2-top-soccer.txt") as a1:
                    for line in a1:
                        file2.write(line)
                a1.close()
                file2.write(divider)
                file2.write(coupon1_soccer)
                file2.write(caveat)
                file2.write(divider)
                with open("soccer-template-parts/email2-static-soccer.txt") as a2:
                    for line in a2:
                        file2.write(line)
                a2.close()
                file2.write(divider)
                file2.write(play_hard)
                file2.write(divider)
                file2.close()
            with open("emails/soccer3.txt", "a+") as file3:
                file3.write(finish_header)
                file3.write(email3_top)
                file3.write(divider)
                file3.write(pre_event_timer_block)
                file3.write(discount_with_button)
                file3.write(divider)
                file3.write(coupon1_soccer)
                file3.write(caveat)
                file3.write(divider)
                with open("soccer-template-parts/email3-body-soccer.txt") as a1:
                    for line in a1:
                        file3.write(line)
                a1.close()
                file3.write(caveat)
                file3.write(divider)
                file3.write(play_hard)
                file3.write(divider)
                file3.close()
            with open("emails/soccer4.txt", "a+") as file4:
                file4.write(finish_header)
                file4.write(email4_top)
                file4.write(divider)
                file4.write(pre_event_timer_block)
                file4.write(discount_with_button)
                file4.write(divider)
                file4.write(coupon1_soccer)
                file4.write(caveat)
                file4.write(divider)
                with open("soccer-template-parts/email3-body-soccer.txt") as a1:
                    for line in a1:
                        file4.write(line)
                a1.close()
                file4.write(caveat)
                file4.write(divider)
                file4.write(play_hard)
                file4.write(divider)
                file4.close()
            with open("emails/soccer5a.txt", "a+") as file5a:
                file5a.write(finish_header)
                file5a.write(email5a_top)
                file5a.write(divider)
                with open("soccer-template-parts/soccer5a-static.txt") as a1:
                    for line in a1:
                        file5a.write(line)
                a1.close()
                file5a.close()
            with open("emails/soccer5.txt", "a+") as file5:
                file5.write(finish_header)
                file5.write(email5_top)
                file5.write(divider)
                with open("soccer-template-parts/soccer5-static.txt") as a1:
                    for line in a1:
                        file5.write(line)
                a1.close()
                file5.write(divider)
                file5.write(play_hard)
                file5.write(divider)
                file5.write(coupon1_soccer)
                file5.close()
            with open("emails/soccer6.txt", "a+") as file6:
                file6.write(finish_header)
                file6.close()
            with open("emails/soccer7.txt", "a+") as file7:
                file7.write(finish_header)
                file7.close()

            #add closing content to all files
            with open("close.txt") as f:
                with open("emails/soccer1.txt", "a+") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/soccer2.txt", "a+") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/soccer3.txt", "a+") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/soccer4.txt", "a+") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/soccer5a.txt", "a+") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/soccer5.txt", "a+") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/soccer6.txt", "a+") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
                f.seek(0, 0)
                with open("emails/soccer7.txt", "a+") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()
            f.close()

            #create Soccer previews

            with open("emails/soccer1.txt") as f:
                with open("templates/soccer1.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/soccer2.txt") as f:
                with open("templates/soccer2.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/soccer3.txt") as f:
                with open("templates/soccer3.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/soccer4.txt") as f:
                with open("templates/soccer4.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/soccer5a.txt") as f:
                with open("templates/soccer5a.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/soccer5.txt") as f:
                with open("templates/soccer5.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/soccer6.txt") as f:
                with open("templates/soccer6.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/soccer7.txt") as f:
                with open("templates/soccer7.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()

        #SOFTBALL TEMPLATES

        if(sport_selection == "Softball"):

            #add header content to all files
            with open("softball-initialize.txt") as f:
                with open("emails/softball1.txt", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/softball2.txt", "w") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/softball3.txt", "w") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/softball4.txt", "w") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/softball5a.txt", "w") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/softball5.txt", "w") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/softball6.txt", "w") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
            f.close()

            with open("initialize7.txt") as f:
                with open("emails/softball7.txt", "w") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()

            #add header
            with open("header-nplogo.txt") as f:
                with open("emails/softball1.txt", "a+") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/softball2.txt", "a+") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/softball3.txt", "a+") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/softball4.txt", "a+") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/softball5a.txt", "a+") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/softball5.txt", "a+") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/softball6.txt", "a+") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
                f.seek(0, 0)
                with open("emails/softball7.txt", "a+") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()
            f.close()

            #add softball body content to all files

            with open("emails/softball1.txt", "a+") as file:
                file.write(finish_header)
                file.write(baseball_top1)
                file.write(divider)
                with open("basesoft-template-parts/basesoft-maximize.txt") as a1:
                    for line in a1:
                        file.write(line)
                a1.close()
                file.write(divider)
                file.write(coupon_basesoft)
                file.write(caveat)
                file.write(divider)
                with open('basesoft-template-parts/softball-highlights.txt') as a2:
                    for line in a2:
                        file.write(line)
                a2.close()
                file.write(divider)
                with open('basesoft-template-parts/showcase-talent.txt') as a3:
                    for line in a3:
                        file.write(line)
                a3.close()
                file.write(divider)
                with open('basesoft-template-parts/soft-showcase-profile.txt') as a4:
                    for line in a4:
                        file.write(line)
                a4.close()
                file.write(divider)
                with open('basesoft-template-parts/be-ready.txt') as a5:
                    for line in a5:
                        file.write(line)
                a5.close()
                file.write(divider)
                with open('basesoft-template-parts/coaches-softball.txt') as a6:
                    for line in a6:
                        file.write(line)
                a6.close()
                file.write(divider)
                file.write(play_hard)
                file.write(divider)
                file.close()
            with open("emails/softball2.txt", "a+") as file2:
                file2.write(finish_header)
                with open('basesoft-template-parts/basesoft-top2.txt') as a1:
                    for line in a1:
                        file2.write(line)
                a1.close()
                file2.write(divider)
                file2.write(coupon_basesoft)
                file2.write(caveat)
                file2.write(divider)
                with open('basesoft-template-parts/email2-visible-proof.txt') as a2:
                    for line in a2:
                        file2.write(line)
                a2.close()
                file2.write(divider)
                with open('basesoft-template-parts/softball-highlights.txt') as a3:
                    for line in a3:
                        file2.write(line)
                a3.close()
                file2.write(divider)
                with open('basesoft-template-parts/soft-showcase-profile.txt') as a4:
                    for line in a4:
                        file2.write(line)
                a4.close()
                file2.write(divider)
                with open('basesoft-template-parts/increase-reach-softball.txt') as a5:
                    for line in a5:
                        file2.write(line)
                a5.close()
                file2.write(divider)
                file2.write(play_hard)
                file2.write(divider)
                file2.close()
            with open("emails/softball3.txt", "a+") as file3:
                file3.write(finish_header)
                with open('basesoft-template-parts/basesoft-top3.txt') as a1:
                    for line in a1:
                        file3.write(line)
                a1.close()
                file3.write(divider)
                file3.write(pre_event_timer_block)
                file3.write(discount_with_button)
                file3.write(divider)
                file3.write(coupon_basesoft)
                file3.write(divider)
                with open('basesoft-template-parts/softball-highlights.txt') as a3:
                    for line in a3:
                        file3.write(line)
                a3.close()
                file3.write(divider)
                with open('basesoft-template-parts/shareable-softball.txt') as a4:
                    for line in a4:
                        file3.write(line)
                a4.close()
                file3.write(divider)
                file3.write(play_hard)
                file3.write(divider)
                file3.close()
            with open("emails/softball4.txt", "a+") as file4:
                file4.write(finish_header)
                file4.write(email4_top_basesoft)
                file4.write(divider)
                file4.write(coupon_basesoft)
                file4.write(caveat)
                file4.write(divider)
                with open('basesoft-template-parts/softball-highlights.txt') as a3:
                    for line in a3:
                        file4.write(line)
                a3.close()
                file4.write(divider)
                with open('basesoft-template-parts/shareable-softball.txt') as a4:
                    for line in a4:
                        file4.write(line)
                a4.close()
                file4.write(divider)
                file4.write(play_hard)
                file4.write(divider)
                file4.close()
            with open("emails/softball5a.txt", "a+") as file5a:
                file5a.write(finish_header)
                file5a.write(email5a_top)
                file5a.write(divider)
                with open('basesoft-template-parts/booth-softball.txt') as a1:
                    for line in a1:
                        file5a.write(line)
                a1.close()
                file5a.write(divider)
                with open('basesoft-template-parts/get_profile_softball.txt') as a2:
                    for line in a2:
                        file5a.write(line)
                a2.close()
                file5a.write(divider)
                with open('basesoft-template-parts/softball-no-time.txt') as a3:
                    for line in a3:
                        file5a.write(line)
                a3.close()
                file5a.write(divider)
                file5a.close()
            with open("emails/softball5.txt", "a+") as file5:
                file5.write(finish_header)
                file5.write(email5_top)
                file5.write(divider)
                with open('basesoft-template-parts/email5-main-softball.txt') as a4:
                    for line in a4:
                        file5.write(line)
                a4.close()
                file5.write(divider)
                with open('basesoft-template-parts/enjoy_game_basesoft.txt') as a5:
                    for line in a5:
                        file5.write(line)
                a5.close()
                file5.write(divider)
                with open('basesoft-template-parts/recruiting_tool_softball.txt') as a6:
                    for line in a6:
                        file5.write(line)
                a6.close()
                file5.write(divider)
                file5.write(coupon_basesoft)
                file5.write(divider)
                file5.write(play_hard)
                file5.write(divider)
                file5.close()
            with open("emails/softball6.txt", "a+") as file6:
                file6.write(finish_header)
                file6.write(email6_top_basesoft)
                file6.write(dark_timer_coupon_basesoft)
                file6.write(caveat2)
                file6.write(divider)
                file6.write(estimated_date)
                with open('basesoft-template-parts/email6-static-softball.txt') as a1:
                    for line in a1:
                        file6.write(line)
                a1.close()
                file6.write(divider)
                file6.write(play_hard)
                file6.write(divider)
                file6.close()
            with open("emails/softball7.txt", "a+") as file7:
                file7.write(finish_header)
                with open("email7_top.txt") as a1:
                    for line in a1:
                        file7.write(line)
                a1.close()
                file7.write(video_block)
                file7.write(divider)
                file7.write(email7_timer_basesoft)
                file7.write(divider)
                with open('basesoft-template-parts/email7-static-softball.txt') as a2:
                    for line in a2:
                        file7.write(line)
                a2.close()
                file7.write(divider)
                with open("testimonials.txt") as a2:
                    for line in a2:
                        file7.write(line)
                a2.close()
                file7.write(divider)
                file7.write(play_hard)
                file7.write(divider)
                file7.close()

            #add closing content to all files
            with open("close.txt") as f:
                with open("emails/softball1.txt", "a+") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/softball2.txt", "a+") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/softball3.txt", "a+") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/softball4.txt", "a+") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/softball5a.txt", "a+") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/softball5.txt", "a+") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/softball6.txt", "a+") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
                f.seek(0, 0)
                with open("emails/softball7.txt", "a+") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()
            f.close()

            #Create Preview Templates Softball

            with open("emails/softball1.txt") as f:
                with open("templates/softball1.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/softball2.txt") as f:
                with open("templates/softball2.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/softball3.txt") as f:
                with open("templates/softball3.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/softball4.txt") as f:
                with open("templates/softball4.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/softball5a.txt") as f:
                with open("templates/softball5a.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/softball5.txt") as f:
                with open("templates/softball5.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/softball6.txt") as f:
                with open("templates/softball6.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/softball7.txt") as f:
                with open("templates/softball7.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()

        #BASEBALL TEMPLATES

        if(sport_selection == "Baseball"):

            #add header content to all files
            with open("baseball-init.txt") as f:
                with open("emails/baseball1.txt", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/baseball2.txt", "w") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/baseball3.txt", "w") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/baseball4.txt", "w") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/baseball5a.txt", "w") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/baseball5.txt", "w") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/baseball6.txt", "w") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
            f.close()

            with open("initialize7.txt") as f:
                with open("emails/baseball7.txt", "w") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()

            #add header
            with open("header-nplogo.txt") as f:
                with open("emails/baseball1.txt", "a+") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/baseball2.txt", "a+") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/baseball3.txt", "a+") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/baseball4.txt", "a+") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/baseball5a.txt", "a+") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/baseball5.txt", "a+") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/baseball6.txt", "a+") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
                f.seek(0, 0)
                with open("emails/baseball7.txt", "a+") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()
            f.close()

            #add baseball body content to all files

            with open("emails/baseball1.txt", "a+") as file:
                file.write(finish_header)
                file.write(baseball_top1)
                file.write(divider)
                with open("basesoft-template-parts/basesoft-maximize.txt") as a1:
                    for line in a1:
                        file.write(line)
                a1.close()
                file.write(divider)
                file.write(coupon_basesoft)
                file.write(caveat)
                file.write(divider)
                with open('basesoft-template-parts/baseball-highlights.txt') as a2:
                    for line in a2:
                        file.write(line)
                a2.close()
                file.write(divider)
                with open('basesoft-template-parts/showcase-talent.txt') as a3:
                    for line in a3:
                        file.write(line)
                a3.close()
                file.write(divider)
                with open('basesoft-template-parts/base-showcase-profile.txt') as a4:
                    for line in a4:
                        file.write(line)
                a4.close()
                file.write(divider)
                with open('basesoft-template-parts/be-ready.txt') as a5:
                    for line in a5:
                        file.write(line)
                a5.close()
                file.write(divider)
                with open('basesoft-template-parts/coaches-baseball.txt') as a6:
                    for line in a6:
                        file.write(line)
                a6.close()
                file.write(divider)
                file.write(play_hard)
                file.write(divider)
                file.close()
            with open("emails/baseball2.txt", "a+") as file2:
                file2.write(finish_header)
                with open('basesoft-template-parts/basesoft-top2.txt') as a1:
                    for line in a1:
                        file2.write(line)
                a1.close()
                file2.write(divider)
                file2.write(coupon_basesoft)
                file2.write(caveat)
                file2.write(divider)
                with open('basesoft-template-parts/email2-visible-proof.txt') as a2:
                    for line in a2:
                        file2.write(line)
                a2.close()
                file2.write(divider)
                with open('basesoft-template-parts/baseball-highlights.txt') as a3:
                    for line in a3:
                        file2.write(line)
                a3.close()
                file2.write(divider)
                with open('basesoft-template-parts/base-showcase-profile.txt') as a4:
                    for line in a4:
                        file2.write(line)
                a4.close()
                file2.write(divider)
                with open('basesoft-template-parts/increase-reach-baseball.txt') as a5:
                    for line in a5:
                        file2.write(line)
                a5.close()
                file2.write(divider)
                file2.write(play_hard)
                file2.write(divider)
                file2.close()
            with open("emails/baseball3.txt", "a+") as file3:
                file3.write(finish_header)
                with open('basesoft-template-parts/basesoft-top3.txt') as a1:
                    for line in a1:
                        file3.write(line)
                a1.close()
                file3.write(divider)
                file3.write(pre_event_timer_block)
                file3.write(discount_with_button)
                file3.write(divider)
                file3.write(coupon_basesoft)
                file3.write(divider)
                with open('basesoft-template-parts/baseball-highlights.txt') as a3:
                    for line in a3:
                        file3.write(line)
                a3.close()
                file3.write(divider)
                with open('basesoft-template-parts/shareable-baseball.txt') as a4:
                    for line in a4:
                        file3.write(line)
                a4.close()
                file3.write(divider)
                file3.write(play_hard)
                file3.write(divider)
                file3.close()
            with open("emails/baseball4.txt", "a+") as file4:
                file4.write(finish_header)
                file4.write(email4_top_basesoft)
                file4.write(divider)
                file4.write(coupon_basesoft)
                file4.write(caveat)
                file4.write(divider)
                with open('basesoft-template-parts/baseball-highlights.txt') as a3:
                    for line in a3:
                        file4.write(line)
                a3.close()
                file4.write(divider)
                with open('basesoft-template-parts/shareable-baseball.txt') as a4:
                    for line in a4:
                        file4.write(line)
                a4.close()
                file4.write(divider)
                file4.write(play_hard)
                file4.write(divider)
                file4.close()
            with open("emails/baseball5a.txt", "a+") as file5a:
                file5a.write(finish_header)
                file5a.write(email5a_top)
                file5a.write(divider)
                with open('basesoft-template-parts/booth-baseball.txt') as a1:
                    for line in a1:
                        file5a.write(line)
                a1.close()
                file5a.write(divider)
                with open('basesoft-template-parts/get_profile_baseball.txt') as a2:
                    for line in a2:
                        file5a.write(line)
                a2.close()
                file5a.write(divider)
                with open('basesoft-template-parts/baseball-no-time.txt') as a3:
                    for line in a3:
                        file5a.write(line)
                a3.close()
                file5a.write(divider)
                file5a.close()
            with open("emails/baseball5.txt", "a+") as file5:
                file5.write(finish_header)
                file5.write(email5_top)
                file5.write(divider)
                with open('basesoft-template-parts/email5-main-baseball.txt') as a4:
                    for line in a4:
                        file5.write(line)
                a4.close()
                file5.write(divider)
                with open('basesoft-template-parts/enjoy_game_basesoft.txt') as a5:
                    for line in a5:
                        file5.write(line)
                a5.close()
                file5.write(divider)
                with open('basesoft-template-parts/recruiting_tool_baseball.txt') as a6:
                    for line in a6:
                        file5.write(line)
                a6.close()
                file5.write(divider)
                file5.write(coupon_basesoft)
                file5.write(divider)
                file5.write(play_hard)
                file5.write(divider)
                file5.close()
            with open("emails/baseball6.txt", "a+") as file6:
                file6.write(finish_header)
                file6.write(email6_top_basesoft)
                file6.write(dark_timer_coupon_basesoft)
                file6.write(caveat2)
                file6.write(divider)
                file6.write(estimated_date)
                with open('basesoft-template-parts/email6-static-baseball.txt') as a1:
                    for line in a1:
                        file6.write(line)
                a1.close()
                file6.write(divider)
                file6.write(play_hard)
                file6.write(divider)
                file6.close()
            with open("emails/baseball7.txt", "a+") as file7:
                file7.write(finish_header)
                with open("email7_top.txt") as a1:
                    for line in a1:
                        file7.write(line)
                a1.close()
                file7.write(video_block)
                file7.write(divider)
                file7.write(email7_timer_basesoft)
                file7.write(divider)
                with open('basesoft-template-parts/email7-static-baseball.txt') as a2:
                    for line in a2:
                        file7.write(line)
                a2.close()
                file7.write(divider)
                with open("testimonials.txt") as a3:
                    for line in a3:
                        file7.write(line)
                a3.close()
                file7.write(divider)
                file7.write(play_hard)
                file7.write(divider)
                file7.close()

            #add closing content to all files
            with open("close.txt") as f:
                with open("emails/baseball1.txt", "a+") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/baseball2.txt", "a+") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/baseball3.txt", "a+") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/baseball4.txt", "a+") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/baseball5a.txt", "a+") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/baseball5.txt", "a+") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/baseball6.txt", "a+") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
                f.seek(0, 0)
                with open("emails/baseball7.txt", "a+") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()
            f.close()

            #Create Preview Templates Baseball

            with open("emails/baseball1.txt") as f:
                with open("templates/baseball1.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/baseball2.txt") as f:
                with open("templates/baseball2.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/baseball3.txt") as f:
                with open("templates/baseball3.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/baseball4.txt") as f:
                with open("templates/baseball4.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/baseball5a.txt") as f:
                with open("templates/baseball5a.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/baseball5.txt") as f:
                with open("templates/baseball5.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/baseball6.txt") as f:
                with open("templates/baseball6.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()
            with open("emails/baseball7.txt") as f:
                with open("templates/baseball7.html", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
            f.close()

        #BASKETBALL TEMPLATES

        if(sport_selection == "Basketball"):

            #add header content to all files
            with open("basketball-init.txt") as f:
                with open("emails/basketball1.txt", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/basketball2.txt", "w") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/basketball3.txt", "w") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/basketball4.txt", "w") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/basketball5a.txt", "w") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/basketball5.txt", "w") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/basketball6.txt", "w") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
            f.close()

            with open("initialize7.txt") as f:
                with open("emails/basketball7.txt", "w") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()

            #add header
            with open("header.txt") as f:
                with open("emails/basketball1.txt", "a+") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/basketball2.txt", "a+") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/basketball3.txt", "a+") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/basketball4.txt", "a+") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/basketball5a.txt", "a+") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/basketball5.txt", "a+") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/basketball6.txt", "a+") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
                f.seek(0, 0)
                with open("emails/basketball7.txt", "a+") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()
            f.close()

            #add body content to all files

            with open("emails/basketball1.txt", "a+") as file:
                file.write(finish_header)
                file.close()
            with open("emails/basketball2.txt", "a+") as file2:
                file2.write(finish_header)
                file2.close()
            with open("emails/basketball3.txt", "a+") as file3:
                file3.write(finish_header)
                file3.close()
            with open("emails/basketball4.txt", "a+") as file4:
                file4.write(finish_header)
                file4.close()
            with open("emails/basketball5a.txt", "a+") as file5a:
                file5a.write(finish_header)
                file5a.close()
            with open("emails/basketball5.txt", "a+") as file5:
                file5.write(finish_header)
                file5.close()
            with open("emails/basketball6.txt", "a+") as file6:
                file6.write(finish_header)
                file6.close()
            with open("emails/basketball7.txt", "a+") as file7:
                file7.write(finish_header)
                file7.close()

            #add closing content to all files
            with open("close.txt") as f:
                with open("emails/basketball1.txt", "a+") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/basketball2.txt", "a+") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/basketball3.txt", "a+") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/basketball4.txt", "a+") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/basketball5a.txt", "a+") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/basketball5.txt", "a+") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/basketball6.txt", "a+") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
                f.seek(0, 0)
                with open("emails/basketball7.txt", "a+") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()
            f.close()

        #FIELD HOCKEY TEMPLATES

        if(sport_selection == "Field Hockey"):

            #add header content to all files
            with open("initialize.txt") as f:
                with open("emails/fieldhockey1.txt", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/fieldhockey2.txt", "w") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/fieldhockey3.txt", "w") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/fieldhockey4.txt", "w") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/fieldhockey5a.txt", "w") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/fieldhockey5.txt", "w") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/fieldhockey6.txt", "w") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
            f.close()

            with open("initialize7.txt") as f:
                with open("emails/fieldhockey7.txt", "w") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()

            #add header
            with open("header.txt") as f:
                with open("emails/fieldhockey1.txt", "a+") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/fieldhockey2.txt", "a+") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/fieldhockey3.txt", "a+") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/fieldhockey4.txt", "a+") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/fieldhockey5a.txt", "a+") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/fieldhockey5.txt", "a+") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/fieldhockey6.txt", "a+") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
                f.seek(0, 0)
                with open("emails/fieldhockey7.txt", "a+") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()
            f.close()

            #add body content to all files

            with open("emails/fieldhockey1.txt", "a+") as file:
                file.write(finish_header)
                file.close()
            with open("emails/fieldhockey2.txt", "a+") as file2:
                file2.write(finish_header)
                file2.close()
            with open("emails/fieldhockey3.txt", "a+") as file3:
                file3.write(finish_header)
                file3.close()
            with open("emails/fieldhockey4.txt", "a+") as file4:
                file4.write(finish_header)
                file4.close()
            with open("emails/fieldhockey5a.txt", "a+") as file5a:
                file5a.write(finish_header)
                file5a.close()
            with open("emails/fieldhockey5.txt", "a+") as file5:
                file5.write(finish_header)
                file5.close()
            with open("emails/fieldhockey6.txt", "a+") as file6:
                file6.write(finish_header)
                file6.close()
            with open("emails/fieldhockey7.txt", "a+") as file7:
                file7.write(finish_header)
                file7.close()

            #add closing content to all files
            with open("close.txt") as f:
                with open("emails/fieldhockey1.txt", "a+") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
                f.seek(0, 0)
                with open("emails/fieldhockey2.txt", "a+") as f2:
                    for line in f:
                         f2.write(line)
                f2.close()
                f.seek(0, 0)
                with open("emails/fieldhockey3.txt", "a+") as f3:
                    for line in f:
                         f3.write(line)
                f3.close()
                f.seek(0, 0)
                with open("emails/fieldhockey4.txt", "a+") as f4:
                    for line in f:
                         f4.write(line)
                f4.close()
                f.seek(0, 0)
                with open("emails/fieldhockey5a.txt", "a+") as f5a:
                    for line in f:
                         f5a.write(line)
                f5a.close()
                f.seek(0, 0)
                with open("emails/fieldhockey5.txt", "a+") as f5:
                    for line in f:
                         f5.write(line)
                f5.close()
                f.seek(0, 0)
                with open("emails/fieldhockey6.txt", "a+") as f6:
                    for line in f:
                         f6.write(line)
                f6.close()
                f.seek(0, 0)
                with open("emails/fieldhockey7.txt", "a+") as f7:
                    for line in f:
                         f7.write(line)
                f7.close()
            f.close()
