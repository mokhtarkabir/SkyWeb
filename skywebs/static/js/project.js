// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // ===== SEARCH & FILTER =====
    const searchInput = document.getElementById('searchInput');
    const categoryFilter = document.getElementById('categoryFilter');
    const templateItems = document.querySelectorAll('.project-item');
  
    function filterTemplates() {
      const searchTerm = searchInput.value.toLowerCase();
      const selectedCategory = categoryFilter.value;
  
      templateItems.forEach(item => {
        const name = item.querySelector('h4').textContent.toLowerCase();
        const category = item.querySelector('p').textContent;
        
        const matchesSearch = name.includes(searchTerm);
        const matchesCategory = (selectedCategory === 'all') || (category === selectedCategory);
  
        if (matchesSearch && matchesCategory) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    }
  
    // Event listeners
    searchInput.addEventListener('input', filterTemplates);
    categoryFilter.addEventListener('change', filterTemplates);
  
    // ===== IFRAME LOADING =====
    // Mark iframes as loaded when they finish loading
    document.querySelectorAll('.template-preview').forEach(iframe => {
      iframe.addEventListener('load', function() {
        this.classList.add('loaded');
      });
    });
  });