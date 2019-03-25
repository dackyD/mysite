from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break, SubMenu

@toolbar_pool.register
class PostToolbar(CMSToolbar):
    
    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu("blog-menu", "Blog")
        
        position = admin_menu.get_alphabetical_insert_position("Posts", SubMenu)
        
        post_menu = admin_menu.get_or_create_menu("post-menu", "Posts", position=position)
        url = "/admin/blog/post"
        post_menu.add_modal_item("Edit Posts", url=url)
        
        url = "/admin/blog/post/add"
        post_menu.add_modal_item("Add New Post", url=url)
        
        post_menu.add_break()
        
@toolbar_pool.register
class CategoryToolbar(CMSToolbar):
    
    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu("blog-menu", "Blog")
        
        position = admin_menu.get_alphabetical_insert_position("Categories", SubMenu)
        
        category_menu = admin_menu.get_or_create_menu("category-menu", "Categories", position=position)
        url = "/admin/blog/category"
        category_menu.add_modal_item("Edit Categories", url=url)
        
        url = "/admin/blog/category/add"
        category_menu.add_modal_item("Add New Category", url=url)
        
        category_menu.add_break()