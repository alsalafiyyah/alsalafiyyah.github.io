# _plugins/active_pagination.rb
#
# Jekyll Active Section & Category Paginator Plugin
#
# Paginates posts for any page that specifies `active: <name>` in its frontmatter:
# ---
# active: audios // videos, muqolat, biography, etc.
# ---

module Jekyll
  class Pagination < Generator
    safe true
    priority :lowest # Run after all pages and posts are loaded

    def generate(site)
      # Check if pagination is disabled in _config.yml
      if site.config['pagination'] && site.config['pagination']['enabled'] == false
        return
      end

      paginate_active_pages(site)
    end

    def paginate_active_pages(site)
      # Duplicate site.pages array to safely append new paginated pages during iteration
      pages_to_paginate = site.pages.dup.select do |page|
        !page.data['active'].nil? && !page.data['active'].to_s.strip.empty?
      end

      # Default paginate size from _config.yml (fallback to 10)
      default_paginate_size = (site.config.dig('pagination', 'paginate') || site.config['paginate'] || 10).to_i

      pages_to_paginate.each do |page|
        # 1. Clean the active key (handles inline comments like "audios // videos...")
        raw_active = page.data['active'].to_s
        active_key = raw_active.split('//').first.strip.downcase

        # 2. Filter posts matching this active key (checks categories, category, tags, and active)
        matching_posts = filter_posts_for_active(site, active_key)

        # 3. Allow page-level pagination limit override: paginate: 5 in frontmatter
        paginate_size = (page.data['paginate'] || default_paginate_size).to_i
        paginate_size = 10 if paginate_size <= 0

        total_pages = (matching_posts.size / paginate_size.to_f).ceil
        total_pages = 1 if total_pages < 1

        # 4. Resolve the base directory for permalinks
        base_dir = resolve_base_dir(page, active_key)

        # 5. Bind Page 1 directly to the existing page
        pager1 = Pager.new(site, 1, matching_posts, total_pages, paginate_size, base_dir)
        page.pager = pager1
        page.data['pager'] = pager1.to_liquid
        page.data['paginator'] = pager1.to_liquid # Compatibility with standard paginator

        # 6. Generate Page 2 through total_pages
        (2..total_pages).each do |current_page|
          pager = Pager.new(site, current_page, matching_posts, total_pages, paginate_size, base_dir)
          paginated_page = ActivePaginationPage.new(site, page, current_page, base_dir)
          paginated_page.pager = pager
          paginated_page.data['pager'] = pager.to_liquid
          paginated_page.data['paginator'] = pager.to_liquid
          site.pages << paginated_page
        end
      end
    end

    # Flexible matching: matches post categories, tags, or post-level active key
    def filter_posts_for_active(site, active_key)
      target = active_key.downcase
      site.posts.docs.select do |post|
        categories = Array(post.data['categories']).flatten.map(&:to_s).map(&:downcase)
        category = post.data['category'] ? [post.data['category'].to_s.downcase] : []
        tags = Array(post.data['tags']).flatten.map(&:to_s).map(&:downcase)
        post_active = post.data['active'].to_s.downcase
        post_type = post.data['type'].to_s.downcase

        (categories + category).include?(target) ||
          tags.include?(target) ||
          post_active == target ||
          post_type == target
      end.reverse
    end

    def resolve_base_dir(page, active_key)
      dir = page.dir.to_s
      if dir.empty? || dir == '/'
        # Check if page has a custom slug or basename
        if page.name.include?('.') && !['index.html', 'index.md'].include?(page.name)
          slug = page.basename
          "/#{slug}"
        else
          "/#{active_key}"
        end
      else
        dir.chomp('/')
      end
    end
  end

  class Pager
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

      # Construct friendly URL paths for Previous & Next pagination buttons
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
      # Clean standard pagination directory: /audios/page/2/index.html
      @dir = "#{base_dir}/page/#{current_page}"
      @name = 'index.html'

      self.process(@name)

      # Inherit frontmatter data, custom layout, and metadata from the parent page
      self.data = base_page.data.dup

      # Update title and pagination flags
      base_title = base_page.data['title'] || base_page.data['active'].to_s.capitalize
      self.data['title'] = "#{base_title} - Page #{current_page}"
      self.data['current_page'] = current_page
      self.data['is_pagination_page'] = true

      # Inherit page content template so custom Liquid layouts render identical markup
      self.content = base_page.content
    end
  end
end
