# _plugins/active_pagination.rb
#
# Jekyll Active Category/Section Paginator Plugin
# Supports pages such as:
#   _pages/audio-fatwas.html (with active: "audios")
# Matches posts with front matter:
#   active: audios

module Jekyll
  class ActivePaginationGenerator < Generator
    safe true
    priority :lowest # Ensures all posts and collections are loaded first

    def generate(site)
      # Find all pages in site.pages (including _pages/) declaring an 'active' key
      pages_to_paginate = site.pages.dup.select do |page|
        val = page.data['active']
        !val.nil? && !val.to_s.strip.empty?
      end

      return if pages_to_paginate.empty?

      # Global paginate size from _config.yml (defaults to 10)
      global_paginate = (site.config.dig('pagination', 'paginate') || site.config['paginate'] || 10).to_i

      pages_to_paginate.each do |page|
        raw_active = page.data['active'].to_s
        active_target = raw_active.split('//').first.strip.downcase

        # 1. Filter posts that have active: audios
        matching_posts = find_posts_for_active(site, active_target)

        # 2. Page-level pagination limit: paginate: 5
        paginate_size = (page.data['paginate'] || global_paginate).to_i
        paginate_size = 10 if paginate_size <= 0

        total_pages = (matching_posts.size / paginate_size.to_f).ceil
        total_pages = 1 if total_pages < 1

        # 3. Base directory for pagination URLs (respects permalink: /audio-fatwas/)
        base_dir = determine_base_dir(page, active_target)

        # 4. Page 1 (The base page)
        pager1 = ActivePager.new(site, 1, matching_posts, total_pages, paginate_size, base_dir)
        page.pager = pager1
        
        # Inject to page.data so both paginator and page.pager work in Liquid layouts
        page.data['pager'] = pager1.to_liquid
        page.data['paginator'] = pager1.to_liquid
        page.data['current_page'] = 1
        page.data['total_pages'] = total_pages

        # 5. Generate subpages (Page 2 through total_pages)
        (2..total_pages).each do |current_page|
          pager = ActivePager.new(site, current_page, matching_posts, total_pages, paginate_size, base_dir)
          paginated_page = ActivePaginationPage.new(site, page, current_page, base_dir)

          paginated_page.pager = pager
          paginated_page.data['pager'] = pager.to_liquid
          paginated_page.data['paginator'] = pager.to_liquid

          site.pages << paginated_page
        end
      end
    end

    def find_posts_for_active(site, target)
      all_posts = site.posts.docs || []

      matching = all_posts.select do |post|
        post_active = post.data['active'].to_s.strip.downcase

        # Checks active: audios, categories, and tags
        categories = Array(post.data['categories']).flatten.map(&:to_s).map(&:downcase)
        category = post.data['category'] ? [post.data['category'].to_s.downcase] : []
        tags = Array(post.data['tags']).flatten.map(&:to_s).map(&:downcase)

        post_active == target ||
          (categories + category).include?(target) ||
          tags.include?(target)
      end

      matching.reverse # Newest posts first
    end

    def determine_base_dir(page, active_target)
      permalink = page.data['permalink'].to_s.strip
      return permalink.chomp('/') unless permalink.empty?

      url = page.url.to_s.strip
      if !url.empty? && url != '/'
        return url.chomp('/').sub(/\/index\.html$/, '').chomp('/')
      end

      dir = page.dir.to_s.strip
      if !dir.empty? && dir != '/'
        return dir.chomp('/')
      end

      "/#{active_target}"
    end
  end

  class ActivePager
    attr_reader :current_page, :total_pages, :total_posts, :per_page,
                :posts, :previous_page, :next_page,
                :previous_page_path, :next_page_path

    def initialize(site, current_page, all_posts, total_pages, paginate_size, base_dir)
      @current_page = current_page
      @total_pages = total_pages
      @total_posts = all_posts.size
      @per_page = paginate_size

      start = (current_page - 1) * paginate_size
      @posts = all_posts.slice(start, paginate_size) || []

      @previous_page = current_page > 1 ? current_page - 1 : nil
      @next_page = current_page < total_pages ? current_page + 1 : nil

      @previous_page_path = if @previous_page
        @previous_page == 1 ? "#{base_dir}/" : "#{base_dir}/page/#{@previous_page}/"
      else
        nil
      end

      @next_page_path = if @next_page
        "#{base_dir}/page/#{@next_page}/"
      else
        nil
      end
    end

    def to_liquid
      {
        'page' => @current_page,
        'current_page' => @current_page,
        'per_page' => @per_page,
        'total_posts' => @total_posts,
        'total_pages' => @total_pages,
        'posts' => @posts,
        'previous_page' => @previous_page,
        'next_page' => @next_page,
        'previous_page_path' => @previous_page_path,
        'next_page_path' => @next_page_path
      }
    end
  end

  class ActivePaginationPage < Page
    attr_accessor :pager

    def initialize(site, base_page, current_page, base_dir)
      @site = site
      @base = site.source
      @dir = "#{base_dir}/page/#{current_page}"
      @name = 'index.html'

      self.process(@name)

      # Clones layout, title, and metadata from _pages/audio-fatwas.html
      self.data = base_page.data.dup

      base_title = base_page.data['title'] || base_page.data['active'].to_s.capitalize
      self.data['title'] = "#{base_title} - Page #{current_page}"
      self.data['current_page'] = current_page
      self.data['is_pagination_page'] = true

      self.content = base_page.content
    end
  end
end