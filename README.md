# Module Preprocessing WYSIWYG

Module untuk *cleaning* HTML Tags

Module ini menggunakan library [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc)

## Prasyarat

- [python](https://www.python.org/downloads/)
- [pip](https://pypi.org/project/pip/)


### install library bs4
`pip install bs4`

### install dependencies
`pip install lxml`

## cara penggunaan
1. import file sebagai module
`import module_preprocessing`
2. gunakan function `cleanHTMLTag` dengan parameter berupa raw html bertipe string
3. function `cleanHTMLTag` akan me-*return* clean text bertipe string
