## JavaScript DOM manipulation
DOM (Document Object Model) manipulation in JavaScript involves interacting with the HTML document structure and updating its content, style, or structure dynamically. Here are some common tasks related to DOM manipulation using JavaScript:
1. Selecting Elements:
* Use document.getElementById('id') to select an element by its ID.
* Use document.querySelector('selector') to select the first element that matches the CSS selector.
* Use document.querySelectorAll('selector') to select all elements that match the CSS selector.
2. Updating Text Content:
* Use the textContent property to update the text content of an element.
javascript
```
const element = document.getElementById('example');
element.textContent = 'New Text Content';
```
3. Updating HTML Content:
* Use the 'innerHTML' property to update the HTML content of an element.
javascript
```
const element = document.getElementById('example');
element.innerHTML = '<strong>New HTML Content</strong>';
```
4. Updating Attribute Values:
* Use the setAttribute method to update the value of an attribute.
javascript
```
const element = document.getElementById('example');
element.setAttribute('src', 'new-image.jpg');
```
5. Styling Elements:
* Use the style property to update CSS styles.
javascript
```
const element = document.getElementById('example');
element.style.color = 'blue';
```
6. Creating New Elements:
* Use document.createElement('tag') to create a new HTML element.
* Use appendChild or insertBefore to add the new element to the document.
javascript
```
const newElement = document.createElement('p');
newElement.textContent = 'New Paragraph';
document.body.appendChild(newElement);
```
7. Event Handling:
* Use addEventListener to attach event handlers to elements.
javascript
```
const button = document.getElementById('myButton');
button.addEventListener('click', function() {
  alert('Button Clicked!');
});
```
8. Removing Elements:
* Use parentNode.removeChild to remove an element.
javascript
```
const elementToRemove = document.getElementById('example');
elementToRemove.parentNode.removeChild(elementToRemove);
```
9. Traversal:
* Use properties like parentNode, nextSibling, and previousSibling to traverse the DOM tree.

These are just some basic examples of DOM manipulation tasks in JavaScript. Depending on your specific requirements, you may need to use a combination of these techniques to achieve more complex manipulations.
