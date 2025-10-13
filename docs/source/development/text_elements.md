# Text elements

General things on how the text and links are handled. 

```{todo}
Provide syntax examples for `rST` and `MD`.
```

## Text formatting

`````{tab-set}
````{tab-item} rST syntax
```{literalinclude} example_files/RSTsyntax_textformatting.rst
```
````

````{tab-item} MD syntax
```{literalinclude} example_files/MDsyntax_textformatting.md
```
````
`````

## Headings

`````{tab-set}
````{tab-item} rST syntax
```{literalinclude} example_files/RSTsyntax_headings.rst
```
````

````{tab-item} MD syntax
```{literalinclude} example_files/MDsyntax_headings.md
```
````
`````

## Links

This is a link to an external webpage:

`````{tab-set}
````{tab-item} rST syntax
```{literalinclude} example_files/RSTsyntax_links.rst
```
:::{attention}
:class: dropdown
Notice the double underscore ``__`` at the end. This is needed to get an anonymous hyperlink reference avoid errors (see [here](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#anonymous-hyperlinks)).
:::
````

````{tab-item} MD syntax
```{literalinclude} example_files/MDsyntax_links.md
```
````
`````

To insert a cross reference to another page/section/paragraph of the wiki, do like this:

`````{tab-set}
````{tab-item} rST syntax
```{literalinclude} example_files/RSTsyntax_crossref.rst
```
````

````{tab-item} MD syntax
```{literalinclude} example_files/MDsyntax_crossref.md
```
````
`````

Here `unique-label` is the **explicit target** that has to be placed before the element that the link is pointing to. In `rST` the explicit target is `.. _unique-label:`; for MD there are different ways to [create an explicit target](https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html#creating-explicit-targets), for example placing `(unique-label)=` before an heading when the target is an heading.

```{important}
:class: dropdown
Always create explicit targets. Do not rely on implicit targets because they can break easily.
```

Finally, note that while in `MD` it is easy to format the link text (for example making it [**bold**](https://www.yambo-code.eu) or [`inline code`](https://www.yambo-code.eu)), this is not possible in `rST`.

## Tables

`````{tab-set}
````{tab-item} rST syntax
```{literalinclude} example_files/RSTsyntax_tables.rst
```
````

````{tab-item} MD syntax
```{literalinclude} example_files/MDsyntax_tables.md
```
````
`````

For more table options in `MD` provided by MyST Parser see [here](https://myst-parser.readthedocs.io/en/latest/syntax/tables.html#tables).
