const section1 = document.querySelector(".section-1");
var scrollTrigger = 60;

window.onscroll = function () {
  // We add pageYOffset for compatibility with IE.
  if (window.scrollY >= scrollTrigger || window.pageYOffset >= scrollTrigger) {
    section1.classList.add("sticky");
  } else {
    section1.classList.remove("sticky");
  }
};

const section3 = document.querySelector(".section-3");
const postBtn = document.querySelector(".post-btn");

postBtn.addEventListener("click", () => {
  // alert("hii");
  let newArticle = document.createElement("div");
  console.log(newArticle);
  newArticle.classList.add("article");
  newArticle.innerHTML = `
        <div class="user-detail">
              <div class="user-profile-pic">
                <img src="../static/assets/profile-pic.png" alt="" />
              </div>
              <div>
                <h3 class="user-name">Rahul kumar</h3>
                <div class="user-credential">
                  Frontend Developer, Student at Gyan Ganga College of
                  Technology
                </div>
              </div>
            </div>
            <p>Official concept art for #SpiderManNoWayHome reveals Tom
            Holland's Spider-Man and Doctor Strange engaging in a battle
            within Tobey Maguire's Spider-Man Universe (Earth-96283)</p>
            <div class="article-img">
              <img src="../static/assets/2.jpeg" alt="" />
            </div>
            <div class="actions">
              <div class="left">
                <button><i class="bi bi-heart"></i></button>
                <button><i class="bi bi-chat"></i></button>
                <button><i class="bi bi-arrow-repeat"></i></button>
              </div>
              <div class="right">
                <button><i class="bi bi-bookmark"></i></button>
                <button><i class="bi bi-three-dots"></i></button>
              </div>
            </div>`;

  section3.insertAdjacentElement("afterBegin", newArticle);
});
