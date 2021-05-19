function toggleDropdownContentVisibility(id) {
    let dropdownContent = getDropdownContent(id);
    if (isDropdownContentVisible(dropdownContent)) {
        hideDropdownContent(dropdownContent);
    } else {
        unhideDropdownContent(dropdownContent);
    }
}

function getDropdownContent(id) {
    let dropdownContent = document.getElementById(id);
    if (dropdownContent == null || dropdownContent == undefined) {
        throw Error('Não existe um elemento com o ID \'' + id + '\' no documento.');
    }
    return dropdownContent;
}

function isDropdownContentVisible(dropdownContent) {
    return !dropdownContent.getAttribute('class').includes('hide');
}

function hideDropdownContent(dropdownContent) {
    dropdownContent.setAttribute('class', dropdownContent.getAttribute('class') + ' hide');
}

function unhideDropdownContent(dropdownContent) {
    let classes = dropdownContent.getAttribute('class').split(' ');
    
    let newClassAttribute = '';
    classes.forEach((class_str) => {
        if (class_str != 'hide') {
            newClassAttribute += class_str;
        }
    });

    dropdownContent.setAttribute('class', newClassAttribute);
}
