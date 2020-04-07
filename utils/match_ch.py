import re

def match_ch(text):
    regex_str = ".*?([\u4E00-\u9FA5]+).*?"
    match_obj = re.findall(regex_str, text)
    return match_obj[0]

a = match_ch('Phylum\tAnnelida\t环节动物门(acc.508, \tsyn.445\t<a class="text-specialists" href="specialist/specialist_details/-2141206354" title="" target="_blank">Lei Yanli</a>)')
print(a)