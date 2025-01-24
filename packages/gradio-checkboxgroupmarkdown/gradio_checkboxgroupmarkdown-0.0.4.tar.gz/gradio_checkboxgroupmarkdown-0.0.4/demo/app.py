import gradio as gr
import random
from typing import List, Dict
from gradio_checkboxgroupmarkdown import CheckboxGroupMarkdown

def generate_test_articles():
    topics = ["Machine Learning", "Deep Learning", "Neural Networks", "Computer Vision", 
              "Natural Language Processing"]
    
    subtopics = ["Introduction", "Tutorial", "Case Study"]
    
    articles = []
    for i in range(10):
        topic = random.choice(topics)
        subtopic = random.choice(subtopics)
        article_id = f"art_{i+1:02d}"
        
        title = f"{topic}: {subtopic}"
        content = f"""# {title}
This article covers {topic.lower()} {subtopic.lower()}.
Key points:
- Basic concepts
- Implementation tips
- Practical examples"""

        articles.append({
            "id": article_id,
            "title": title,
            "content": content,
            "selected": False
        })
    
    return articles

def search_articles(search_text: str, master_articles: List[Dict]) -> List[Dict]:
    print("search_articles")
    
    """Search articles based on input text"""
    if not search_text.strip():
        return master_articles
    
    search_terms = search_text.lower().split()
    filtered_articles = []
    
    for article in master_articles:
        text_to_search = (article["title"] + " " + article["content"]).lower()
        if all(term in text_to_search for term in search_terms):
            filtered_articles.append(article)
    
    return filtered_articles

def update_filtered_articles(search_text: str, master_articles: List[Dict]):
    print("update_filtered_articles")
    
    """Update the first CheckboxGroupMarkdown with filtered articles"""
    filtered = search_articles(search_text, master_articles)
    
    return {
        filtered_checkbox: gr.update(
            choices=filtered,
            value=[art["id"] for art in filtered if art["selected"]]
        ),
        filtered_checkbox_state: filtered
    }
    
def update_selected_checkbox_articles(selected_choices, filtered_checkbox, master_articles: List[Dict]):
    print("handle_deselect_articles")
    
    """Update master articles by removing unselected ones"""
    # Get IDs of articles that remain selected
    selected_ids = {choice["id"] for choice in selected_choices}
    
    # Update selection status in master_articles
    for article in master_articles:
        article["selected"] = article["id"] in selected_ids
            
    # Update selection status in filtered_checkbox
    for article in filtered_checkbox:
        article["selected"] = article["id"] in selected_ids
        
    # Get selected articles for second tab
    selected_articles = [
        {
            "id": art["id"],
            "title": art["title"],
            "content": art["content"],
            "selected": True
        }
        for art in master_articles 
        if art["selected"]
    ]
    
    return [
        gr.update(
            choices=selected_articles,
            value=[art["id"] for art in selected_articles]
        ),
        gr.update(
            value=[art["id"] for art in filtered_checkbox if art["selected"]]
        ),
        master_articles,
        filtered_checkbox
    ]

def update_filtered_checkbox_articles(selected_choices, filtered_checkbox, master_articles: List[Dict]):
    print("update_selected_articles")
    
    """Update the second CheckboxGroupMarkdown when selections change in the first one"""
    # Get IDs of newly selected articles
    selected_ids = {choice["id"] for choice in selected_choices}
    
    # Update selection status in filtered_checkbox_state
    for article in filtered_checkbox:
        if article["id"] in selected_ids:
            article["selected"] = True
        else:
            article["selected"] = False
            
    # Update selection status in master_articles based on filtered_checkbox
    filtered_articles_dict = {art["id"]: art["selected"] for art in filtered_checkbox}
    for article in master_articles:
        if article["id"] in filtered_articles_dict:
            article["selected"] = filtered_articles_dict[article["id"]]
    
    # Get all selected articles for the second component
    selected_articles = [
        {
            "id": art["id"],
            "title": art["title"],
            "content": art["content"],
            "selected": True
        }
        for art in master_articles 
        if art["selected"]
    ]
    
    return {
        selected_checkbox: gr.update(
            choices=selected_articles,
            value=[art["id"] for art in selected_articles]
        ),
        filtered_checkbox_state: filtered_checkbox,
        master_articles_state: master_articles
    }

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Article Search and Selection Demo")
    
    # Create state to hold master articles list
    master_articles_state = gr.State(generate_test_articles())
    filtered_checkbox_state = gr.State(master_articles_state.value)
    print("generate articles")
    
    # Search bar
    with gr.Row():
        search_input = gr.Textbox(
            label="Search Articles",
            placeholder="Enter search terms...",
            show_label=True
        )
        search_button = gr.Button("Search")
    
    # Tabs for the two CheckboxGroupMarkdown components
    with gr.Tabs() as tabs:
        with gr.Tab("Search Results"):
            filtered_checkbox = CheckboxGroupMarkdown(
                choices=master_articles_state.value,
                label="Available Articles",
                info="Select articles to add to your collection",
                type="all",
                value=[art["id"] for art in master_articles_state.value if art["selected"]],
                buttons=["select_all", "deselect_all"]
            )
        print("filtered_checkbox")
        
        with gr.Tab("Selected Collection"):
            selected_checkbox = CheckboxGroupMarkdown(
                choices=[art for art in master_articles_state.value if art["selected"]],
                label="Your Selected Articles",
                info="Your curated collection of articles",
                type="all",
                value=[art["id"] for art in master_articles_state.value if art["selected"]],
                buttons=["select_all", "deselect_all"]
            )
        print("selected_checkbox")
    
    # Event handlers
    search_button.click(
        fn=update_filtered_articles,
        inputs=[search_input, master_articles_state],
        # outputs=[filtered_checkbox, master_articles_state]
        outputs=[filtered_checkbox, filtered_checkbox_state]
    )
    
    filtered_checkbox.select(
        fn=update_filtered_checkbox_articles,
        inputs=[filtered_checkbox, filtered_checkbox_state, master_articles_state],
        outputs=[selected_checkbox, filtered_checkbox_state, master_articles_state]
    )
    
    selected_checkbox.select(
        fn=update_selected_checkbox_articles,
        inputs=[selected_checkbox, filtered_checkbox_state, master_articles_state],
        outputs=[selected_checkbox, filtered_checkbox, master_articles_state, filtered_checkbox_state]
    )
    print("Block")
    

if __name__ == "__main__":
    demo.launch()