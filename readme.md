The **Dream Icons** project is a open repository of lightweight, hand-crafted svg icons for use in applications where clean, modern style and load performance is of paramount importance. All dream icons are CC0 licensing, which means not only are they copyright-free, but they are attribution free as well. Feel free to use them in whatever project and capacity you'd like, no attribution required!

All icons come in one of two types: **external** and **inline**. 

**External** can be used directly in an any html tags, no fuss about it! Just set your `src`, width and height, and you're good to go! External svgs also carry the benefit of easy caching in the browser to prevent the browser from reloading the image in multi-page applications. The downside to this approach is that dynamic styling with css is not an option.

**Inline** cannot be used directly in an `<img>` tag or an `<object>` tag with the type `image/svg+xml` because they have no xmlns attribute. Inlining also prevents the caching of the svg for quicker loads on multi-page applications. However, it does come with a size reduction for single-page and the benefit of stylizing the svg directly in the html document with css stylings!

Hopefully that's enough to get you started using Dream icons in your next project.

*Happy coding!*
