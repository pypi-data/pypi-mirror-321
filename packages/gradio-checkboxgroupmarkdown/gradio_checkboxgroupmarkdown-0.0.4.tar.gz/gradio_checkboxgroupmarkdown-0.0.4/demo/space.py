
import gradio as gr
from app import demo as app
import os

_docs = {'CheckboxGroupMarkdown': {'description': 'Creates a set of checkboxes. Can be used as an input to pass a set of values to a function or as an output to display values, a subset of which are selected.', 'members': {'__init__': {'choices': {'type': 'list[dict] | None', 'default': 'None', 'description': 'A list of string or numeric options to select from. An option can also be a tuple of the form (name, value), where name is the displayed name of the checkbox button and value is the value to be passed to the function, or returned by the function.'}, 'value': {'type': 'Sequence[str | float | int]\n    | str\n    | float\n    | int\n    | Callable\n    | None', 'default': 'None', 'description': 'Default selected list of options. If a single choice is selected, it can be passed in as a string or numeric type. If callable, the function will be called whenever the app loads to set the initial value of the component.'}, 'type': {'type': 'ChoiceType', 'default': '"value"', 'description': 'Type of value to be returned by component. "value" returns the list of strings of the choices selected, "index" returns the list of indices of the choices selected.'}, 'buttons': {'type': 'Optional[List[str]]', 'default': 'None', 'description': None}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'the label for this component, displayed above the component if `show_label` is `True` and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component corresponds to.'}, 'info': {'type': 'str | None', 'default': 'None', 'description': 'additional component description, appears below the label in smaller font. Supports markdown / HTML syntax.'}, 'every': {'type': 'Timer | float | None', 'default': 'None', 'description': 'Continously calls `value` to recalculate it if `value` is a function (has no effect otherwise). Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.'}, 'inputs': {'type': 'Component | Sequence[Component] | set[Component] | None', 'default': 'None', 'description': 'Components that are used as inputs to calculate `value` if `value` is a function (has no effect otherwise). `value` is recalculated any time the inputs change.'}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'If True, will display label.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'Relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'Minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': 'If True, choices in this checkbox group will be checkable; if False, checking will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'key': {'type': 'int | str | None', 'default': 'None', 'description': 'if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.'}}, 'postprocess': {'value': {'type': 'list[str | int | float] | str | int | float | None', 'description': 'Expects a `list[str | int | float]` of values or a single `str | int | float` value, the checkboxes with these values are checked.'}}, 'preprocess': {'return': {'type': 'typing.Union[list[str], list[int], list[dict]][\n    list[str], list[int], list[dict]\n]', 'description': 'Passes the list of checked checkboxes as a `list[str | int | float]` or their indices as a `list[int]` into the function, depending on `type`.'}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the CheckboxGroupMarkdown changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'input': {'type': None, 'default': None, 'description': 'This listener is triggered when the user changes the value of the CheckboxGroupMarkdown.'}, 'select': {'type': None, 'default': None, 'description': 'Event listener for when the user selects or deselects the CheckboxGroupMarkdown. Uses event data gradio.SelectData to carry `value` referring to the label of the CheckboxGroupMarkdown, and `selected` to refer to state of the CheckboxGroupMarkdown. See EventData documentation on how to use this event data'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'CheckboxGroupMarkdown': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_checkboxgroupmarkdown`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/gradio_checkboxgroupmarkdown/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_checkboxgroupmarkdown"></a>  
</div>

Gradio component for CheckboxGroup with Markdown
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_checkboxgroupmarkdown
```

## Usage

```python
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
        content = f\"\"\"# {title}
This article covers {topic.lower()} {subtopic.lower()}.
Key points:
- Basic concepts
- Implementation tips
- Practical examples\"\"\"

        articles.append({
            "id": article_id,
            "title": title,
            "content": content,
            "selected": False
        })
    
    return articles

def search_articles(search_text: str, master_articles: List[Dict]) -> List[Dict]:
    print("search_articles")
    
    \"\"\"Search articles based on input text\"\"\"
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
    
    \"\"\"Update the first CheckboxGroupMarkdown with filtered articles\"\"\"
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
    
    \"\"\"Update master articles by removing unselected ones\"\"\"
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
    
    \"\"\"Update the second CheckboxGroupMarkdown when selections change in the first one\"\"\"
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
```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `CheckboxGroupMarkdown`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["CheckboxGroupMarkdown"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["CheckboxGroupMarkdown"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, passes the list of checked checkboxes as a `list[str | int | float]` or their indices as a `list[int]` into the function, depending on `type`.
- **As output:** Should return, expects a `list[str | int | float]` of values or a single `str | int | float` value, the checkboxes with these values are checked.

 ```python
def predict(
    value: typing.Union[list[str], list[int], list[dict]][
    list[str], list[int], list[dict]
]
) -> list[str | int | float] | str | int | float | None:
    return value
```
""", elem_classes=["md-custom", "CheckboxGroupMarkdown-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          CheckboxGroupMarkdown: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
