import qrcode

test = qrcode.make("https://www.linkedin.com/search/results/all/?fetchDeterministicClustersOnly=true&heroEntityKey=urn%3Ali%3Afsd_profile%3AACoAAEqxNsYBT4Kv_zybm_lTTUuyLxJeV0vrDN0&keywords=salman%20faris&origin=RICH_QUERY_SUGGESTION&position=0&searchId=f170c04e-8efb-4b8f-b3f6-3927fb1601ca&spellCorrectionEnabled=false")
test.save("my_link_qr.png")
