# Taken from https://github.com/gacha/gacha.id.lv/blob/master/_plugins/i18n_filter.rb

require 'i18n'
https://github.com/svenfuchs/rails-i18n/tree/master/rails/locale
# Create folder "_locales" and put some locale file from https://github.com/svenfuchs/rails-i18n/tree/master/rails/locale
module Jekyll
  # i18n filter for jekyll
  module I18nFilter
    # Example:
    #   {{ post.date | localize: "%d.%m.%Y" }}
    #   {{ post.date | localize: ":short" }}
    def localize(input, format = nil, locale = nil)

			# Side effects: changes I18n.config, must run before current_locale is set 
      load_translations

			input = Time.at(input) if input.class == Integer 

      format = format =~ /^:(\w+)/ ? Regexp.last_match(1).to_sym : format

			if input && locale = current_locale(locale) 

				I18n.locale = locale
				I18n.l(input, format: format) 
			else 
				input
			end
		end

    def load_translations
      return false unless I18n.backend.send(:translations).empty?
      filename = File.join(File.dirname(__FILE__), '../_locales/*.yml')
			I18n.backend.load_translations Dir[filename]
    end
		
		def current_locale(locale)
			l = locale || @context.registers[:page]["lang"] || @context.registers[:site].config["lang"]
				
			if l && I18n.config.available_locales.include?(l.to_sym)
				l
			else
				false
			end
		end
	
  end
end

Liquid::Template.register_filter(Jekyll::I18nFilter)
