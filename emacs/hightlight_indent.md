## hightlight mode for emacs
my aim was to emulate my favourite text editor in everyway
One feature that I really like is the column indent mode that shows each vertical lines 

This emacs functionality is provided by several packages 
link to them


- (indent-guide ) https://github.com/DarthFennec/highlight-indent-guides

- ( hightlight indent guides) https://github.com/DarthFennec/highlight-indent-guides/tree/cf352c85cd15dd18aa096ba9d9ab9b7ab493e8f6

- https://github.com/antonj/Highlight-Indentation-for-Emacs/

## in order to separate the lines with vertical bars use the following

``` python

(add-hook 'prog-mode-hook 'highlight-indent-guides-mode)
(setq highlight-indent-guides-method 'character)
(setq highlight-indent-guides-character ?|)



```

all the instrunction are in the .el file (highlight-indent-guides)