
# MIT Licence

# _plugins/jekyll-cleaner-urls.rb

module Jekyll

  class Post

    #https://github.com/jekyll/jekyll/blob/master/lib/jekyll/post.rb
    def id
      File.join(dir, slug).gsub(" ","-").gsub("%20","-").gsub("--","-")
    end

  end

  #https://github.com/jekyll/jekyll/blob/master/lib/jekyll/url.rb
  class URL

    def self.escape_path(path)
      URI.escape(path, /[^a-zA-Z\d\-._~!$&'()*+,;=:@\/]/).encode('utf-8').gsub("%20","-").gsub(" ","-").gsub("--","-")
end

  end

end
