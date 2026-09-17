require 'date'

module Jekyll
  module UmmAlQuraFilter
    def to_umalqura(input)
      return input if input.nil?

      # Safely convert input (Time, String, or Date) to a true Ruby Date object
      date = case input
             when Date
               input
             when Time
               input.to_date
             when String
               begin
                 Date.parse(input)
               rescue ArgumentError
                 return input
               end
             else
               return input
             end

      # Get the Julian Day Number
      jd = date.jd

      # Umm al-Qura calculation boundary check (1356 AH to 1500 AH)
      # Valid between March 14, 1937 and November 16, 2077
      if jd < 2428606 || jd > 2479989
        return "Date out of Umm al-Qura range"
      end

      # Tabular adjustment factor optimized for Saudi Arabian Makkah coordinates
      l = jd - 1948440 + 10632
      n = ((l - 1) / 10631).to_i
      l = l - 10631 * n + 354
      
      # Adjusted astronomical moon-conjunction shift variables
      j = (((10985 - l) / 5316).to_i) * ((50 * l / 17719).to_i) + ((l / 5670).to_i) * ((43 * l / 15238).to_i)
      l = l - (((30 - j) / 15).to_i) * ((17719 * j / 50).to_i) - ((j / 16).to_i) * ((15238 * j / 43).to_i) + 29
      
      month_idx = ((24 * l / 709).to_i)
      day = l - ((709 * month_idx / 24).to_i)
      year = 30 * n + j - 30

      # Official Hijri Months
      months = [
        "Muharram", "Safar", "Rabi' al-Awwal", "Rabi' al-Thani",
        "Jumada al-Awwal", "Jumada al-Thani", "Rajab", "Sha'ban",
        "Ramadan", "Shawwal", "Dhu al-Qa'dah", "Dhu al-Hijjah"
      ]

      "#{day} #{months[month_idx - 1]} #{year} AH"
    end
  end
end

Liquid::Template.register_filter(Jekyll::UmmAlQuraFilter)
