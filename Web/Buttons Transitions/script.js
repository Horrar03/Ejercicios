// Corrección 1: Selector cambiado a '.container button'
const tags = document.querySelectorAll('.container button'); 
const search = document.querySelector('.search');
const tagsContainer = document.querySelector('.tags');

tags.forEach((tag, index) => {
    tag.style.viewTransitionName = `tag-${index}`;
    tag.style.order = index;
});

tagsContainer.addEventListener(
    'click', (e) => {
        const button = e.target.closest('button');
        if (button) {
            document.startViewTransition(() => {
                search.appendChild(button);
            });
        }
    }
);

search.addEventListener(
    'click', (e) => {
        const i = e.target.closest('i');
        if (i) {
            const button = i.closest('button');
            document.startViewTransition(() => {
                tagsContainer.appendChild(button);
            });
        }
    }
);
