module Jekyll
module ArabicDates
    MONTHS = {"01" => "يناير", "02" => "فبراير", "03" => "مارس",
            "04" => "أبريل", "05" => "مايو", "06" => "يونيو",
            "07" => "يوليو", "08" => "أغسطس", "09" => "سبتمبر",
            "10" => "أكتوبر", "11" => "نوفمبر", "12" => "ديسمبر"}
    
  # https://stackoverflow.com/questions/51558710/translating-jekyll-dates
    # http://man7.org/linux/man-pages/man3/strftime.3.html
    def arabicDate(date)
        day = time(date).strftime("%e") 
        month = time(date).strftime("%m")
        year = time(date).strftime("%Y")
        day+' '+MONTHS[month]+' '+year
    end

    def html5date(date)
        day = time(date).strftime("%d")
        month = time(date).strftime("%m")
        year = time(date).strftime("%Y")
        year+'-'+month+'-'+day
    end
end
end

Liquid::Template.register_filter(Jekyll::ArabicDates)
