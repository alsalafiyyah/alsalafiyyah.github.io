require 'fileutils'

module Filter
  def self.process(site, payload)
    site.collections['posts'].docs.select{|x| x.data['auto_image']}.each do |post|

      # Set the path where the copied content will live
      path = './_previews/' + post.data['slug'] + '.md'

      # Copy the content of the post to the preview collection
      File.write(path, File.read(post.path))

      # Create a new document in the preview collection
      preview_doc = Jekyll::Document.new(
        path,
        {site: site, collection: site.collections['previews']}
      )

      preview_doc.read

      # Set the layout to preview
      preview_doc.data['layout'] = 'preview'

      # Add document to the collection
      site.collections['previews'].docs << preview_doc
      
    end
  end
end

Jekyll::Hooks.register :site, :post_read do |site, payload|
  # If the site is being served locally
  # skip generating previews
  # Otherwise there'll be an endless loop of previews being
  # written and regenerated
  if !site.config['serving']
    Filter.process(site, payload)
  end
end

module RemovePreviews
  def self.process(site, payload)
    FileUtils.rm_rf("./_previews/.", secure: true)
  end
end
