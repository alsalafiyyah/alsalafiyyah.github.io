module DateFilter
  MONTHS = %w(Muharram Safar Rabi1 Rabi2 Juma1 Juma2 Rajab Shaban Ramadan Shawwal DhulQadah DhulHijjah)

  def hijri_month(input)
    MONTHS[input.strftime("%m").to_i - 1]
  end
end

Liquid::Template.register_filter(DateFilter)
