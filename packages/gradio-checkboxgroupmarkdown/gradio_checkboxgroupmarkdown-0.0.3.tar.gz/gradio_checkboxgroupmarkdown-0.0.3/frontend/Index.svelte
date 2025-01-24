<svelte:options immutable={true} />

<script lang="ts">
  import type { Gradio, SelectData } from "@gradio/utils";
  import { Block, BlockTitle } from "@gradio/atoms";
  import { BaseButton } from "@gradio/button";
  import { StatusTracker } from "@gradio/statustracker";
  import type { LoadingStatus } from "@gradio/statustracker";
  import { BaseMarkdown } from "@gradio/markdown";

  export let gradio: Gradio<{
    change: never;
    select: SelectData;
    input: never;
    clear_status: LoadingStatus;
  }>;
  export let elem_id = "";
  export let elem_classes: string[] = [];
  export let visible = true;
  export let value: (string | number)[] = [];
  export let choices: {
    id: string;
    title: string;
    content: string;
    selected?: boolean;
  }[] = [];
  export let buttons: Array<string> = [];
  export let container = true;
  export let scale: number | null = null;
  export let min_width: number | undefined = undefined;
  export let label = gradio.i18n("checkbox.checkbox_group");
  export let info: string | undefined = undefined;
  export let show_label = true;
  export let root: string;

  export let loading_status: LoadingStatus;
  export let interactive = true;
  export let old_value = value.slice();

  // markdown props
  export let rtl = false;
  export let latex_delimiters: {
    left: string;
    right: string;
    display: boolean;
  }[];

  function toggle_choice(choice: string): void {
    if (value.includes(choice)) {
      value = value.filter((v) => v !== choice);
    } else {
      value = [...value, choice];
    }

    // Update the selected property in choices
    choices = choices.map((c) => ({
      ...c,
      selected: value.includes(c.id),
    }));

    gradio.dispatch("input");
  }

  $: disabled = !interactive;

  $: if (JSON.stringify(old_value) !== JSON.stringify(value)) {
    old_value = value;
    gradio.dispatch("change");
  }

  function handleSelectAll(select: boolean) {
    const newValue = select ? choices.map((c) => c.id) : [];
    value = newValue;
    gradio.dispatch("change");
  }
</script>

<Block
  {visible}
  {elem_id}
  {elem_classes}
  type="fieldset"
  {container}
  {scale}
  {min_width}
>
  <StatusTracker
    autoscroll={gradio.autoscroll}
    i18n={gradio.i18n}
    {...loading_status}
    on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
  />
  <BlockTitle {root} {show_label} {info}>{label}</BlockTitle>

  <div class="header-container">
    {#if buttons && buttons.length > 0}
      <div class="button-container">
        {#if buttons.includes("select_all")}
          <BaseButton
            size="sm"
            variant="secondary"
            on:click={() => handleSelectAll(true)}
          >
            Select All
          </BaseButton>
        {/if}
        {#if buttons.includes("deselect_all")}
          <BaseButton
            size="sm"
            variant="secondary"
            on:click={() => handleSelectAll(false)}
          >
            Deselect All
          </BaseButton>
        {/if}
      </div>
    {/if}
  </div>

  <div class="wrap" data-testid="checkbox-group">
    {#key choices}
      <!-- Add key to force re-render when choices change -->
      {#each choices as choice, i}
        <label
          class="choice-container {disabled ? 'disabled' : ''} {value.includes(
            choice.id
          )
            ? 'selected'
            : ''}"
        >
          <div class="choice-header">
            <input
              {disabled}
              on:change={() => toggle_choice(choice.id)}
              on:input={(evt) =>
                gradio.dispatch("select", {
                  index: i,
                  value: choice.id,
                  selected: evt.currentTarget.checked,
                })}
              on:keydown={(event) => {
                if (event.key === "Enter") {
                  toggle_choice(choice.id);
                  gradio.dispatch("select", {
                    index: i,
                    value: choice.id,
                    selected: !value.includes(choice.id),
                  });
                }
              }}
              checked={value.includes(choice.id)}
              type="checkbox"
              name={choice.id?.toString()}
              title={choice.title?.toString()}
            />
            <span class="choice-title">{choice.title}</span>
          </div>

          <div class="choice-content">
            <BaseMarkdown
              value={choice.content}
              {elem_classes}
              {visible}
              {rtl}
              {latex_delimiters}
              root={gradio.root}
              {loading_status}
            />
          </div>
        </label>
      {/each}
    {/key}
  </div>
</Block>

<style>
  .wrap {
    display: flex;
    flex-direction: column;
    gap: var(--checkbox-label-gap);
  }
  label {
    display: flex;
    align-items: center;
    transition: var(--button-transition);
    cursor: pointer;
    box-shadow: var(--checkbox-label-shadow);
    border: var(--checkbox-label-border-width) solid
      var(--checkbox-label-border-color);
    border-radius: var(--checkbox-border-radius);
    background: var(--checkbox-label-background-fill);
    padding: var(--checkbox-label-padding);
    color: var(--checkbox-label-text-color);
    font-weight: var(--checkbox-label-text-weight);
    font-size: var(--checkbox-label-text-size);
    line-height: var(--line-md);
    width: 100%;
  }

  label:hover {
    background: var(--checkbox-label-background-fill-hover);
  }
  label:focus {
    background: var(--checkbox-label-background-fill-focus);
  }
  label.selected {
    background: var(--checkbox-label-background-fill-selected);
    color: var(--checkbox-label-text-color-selected);
    border-color: var(--checkbox-label-border-color-selected);
  }

  label > * + * {
    margin-left: var(--size-2);
  }

  input {
    --ring-color: transparent;
    position: relative;
    box-shadow: var(--checkbox-shadow);
    border: var(--checkbox-border-width) solid var(--checkbox-border-color);
    border-radius: var(--checkbox-border-radius);
    background-color: var(--checkbox-background-color);
    line-height: var(--line-sm);
  }

  input:checked,
  input:checked:hover,
  input:checked:focus {
    border-color: var(--checkbox-border-color-selected);
    background-image: var(--checkbox-check);
    background-color: var(--checkbox-background-color-selected);
  }

  input:checked:focus {
    border-color: var(--checkbox-border-color-focus);
    background-image: var(--checkbox-check);
    background-color: var(--checkbox-background-color-selected);
  }

  input:hover {
    border-color: var(--checkbox-border-color-hover);
    background-color: var(--checkbox-background-color-hover);
  }

  input:not(:checked):focus {
    border-color: var(--checkbox-border-color-focus);
  }

  input[disabled],
  .disabled {
    cursor: not-allowed;
  }

  input:hover {
    cursor: pointer;
  }

  .choice-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start; /* Left align items instead of center */
    margin: 0.5em 0;
  }

  .choice-header {
    display: flex;
    width: 100%;
    align-items: center; /* Just aligns items along the cross-axis, not centering horizontally */
    margin-bottom: 0.5em;
  }

  .choice-header input {
    margin-right: 0.5em; /* Space between checkbox and title */
  }

  .choice-title {
    /* By default, text will be left-aligned */
  }

  .choice-content {
    padding-left: 1.5em;
    width: 100%;
  }

  .disabled {
    opacity: 0.5;
  }

  .selected {
    font-weight: bold;
  }

  .header-container {
    display: flex;
    justify-content: flex-end;
    align-items: flex-start;
    margin-bottom: var(--spacing-lg);
    width: 100%;
  }

  .button-container {
    display: flex;
    gap: var(--spacing-sm);
    justify-content: flex-end;
    min-width: fit-content;
  }
</style>
