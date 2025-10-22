const carousel = document.getElementById("dwhCarousel");
if (carousel) {
    let scrollAmount = 0;
    const maxScroll = carousel.scrollWidth - carousel.clientWidth;

    function autoScroll() {
        if (scrollAmount < maxScroll) {
            scrollAmount += 1;
        } else {
            scrollAmount = 0;
        }
        carousel.scrollTo({ left: scrollAmount, behavior: "smooth" });
    }
    setInterval(autoScroll, 30);
}
