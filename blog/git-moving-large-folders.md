# How To Evict Gigantic Folders From Your Git Repo Without Crying Into Your Keyboard

If you’ve ever opened your Git repo, looked at the folder sizes, and felt the same dread as opening your closet before a move, congratulations: you’re living the authentic developer experience. Repos expand. They bloat. They hoard files from 2017 that nobody remembers adding. And one day, when **git push** starts taking longer than a government construction project, you realize something must be done.

Today, we’re going to talk about moving big folders out of one repo, parking them safely in another repo, pushing them to GitHub, and reclaiming enough disk space to make your laptop sigh with relief.

This is the story of digital downsizing, version-control spring cleaning, and why Git sometimes behaves like that friend who insists on bringing the entire 87-piece camping set to a one-night Airbnb.

---

## Why Git Stores Everything Forever (Even When You Tell It To Stop)

The thing about Git is that it’s like a memory elephant. You delete a file? Git still remembers it. You delete a folder? Git still remembers it. You delete your hopes, your dreams, your entire node_modules directory? Git definitely still remembers it.

This is because Git stores history in a way that’s fantastic for archaeologists and time travelers, but less fantastic when you accidentally commit 14 GB of video files for a prototype that lasted six minutes.

So when you want to **move big folders out of one repo into another**, there are really two missions:

1. Move the files to a new repo so you can still push, share, clone, etc.
2. Remove their entire history from the first repo so it stops hogging disk like a golden retriever sitting on your legs.

---

## Step 1: Create the New Repo (Your Files’ New Apartment)

Start by creating a new repo on GitHub. You can use the GitHub UI. No need for anything fancy—just a standard-issue repository that will adopt your large files lovingly and without judgment.

Once created, clone it locally:

```
git clone https://github.com/youruser/new-repo.git
```

Now you have an empty home ready for your migrating folders. Let’s bring in the tenants.

---

## Step 2: Move the Folders (The Ones That Outgrew Their Old Neighborhood)

From your original repo:

```
mv big-folder-1 ../new-repo/
mv big-folder-2 ../new-repo/
```

Or if you prefer copying then deleting later:

```
cp -R big-folder-1 ../new-repo/
```

Once the folders are in the new repo, commit them:

```
cd ../new-repo
git add .
git commit -m "Add large folders"
git push
```

Boom. They’re now happily living in a new repo where they are free to be as large as they want, like whales in an ocean instead of whales in a bathtub.

---

## Step 3: Remove the Folders From the Old Repo (And Actually Get the Space Back)

Now comes the part that Git, in its loving stubbornness, won’t do automatically: **forgetting**.

Deleting folders the normal way does NOT shrink the repo. It simply removes the files from the working directory—while the repo whispers, “but I remember everything.”

To truly remove all traces from history, use **git filter-repo**, GitHub’s modern recommendation replacing the older and more temperamental BFG and filter-branch. You can get it via **[git filter-repo](https://github.com/newren/git-filter-repo)**.

To remove a folder from all history:

```
git filter-repo --path big-folder-1 --invert-paths
```

If there are multiple folders:

```
git filter-repo --path big-folder-1 --path big-folder-2 --invert-paths
```

Now Git will rewrite the entire repo history without those folders, as though they never existed. Like digital witness protection.

Once done, force push the cleaned repo:

```
git push --force
```

Note: This rewrites history. If your repo has multiple collaborators, you will receive 47 messages asking why everything broke. Send them this blog.

---

## Step 4: Celebrate the Dramatic Weight Loss

Check the repo size before and after. Your repo will have shed gigabytes, emotionally and physically lighter, finally free of its baggage.

Calls will be faster.

Pushes will be smoother.

Your storage will sigh and whisper: “thank you.”

---

## Step 5: Put Up a Little Sign That Says “Please Don’t Add Gigantic Files Again”

You can avoid future repo bloating with:

* A `.gitignore` file
* Git LFS (Large File Storage), if storing big binaries
* A stern Slack message in ALL CAPS
* A framed print above your desk that reads: “Thou Shalt Not Commit 4K Footage Into The Backend Repo”

Git LFS is especially useful and worth exploring if your life involves giant media, datasets, or anything that would melt a normal repo. GitHub has solid docs on it at **[Git LFS](https://git-lfs.github.com/)**.

---

## Step 6: Tell Your Friends, Win Their Awe, Earn Internet Points

People LOVE hearing stories about repos that were 14 GB and are now 120 MB. It’s digital weight-loss reality TV—except this time, you’re the star.

If this helped you, drop a comment, share your funniest repo-bloat story, or follow along for more tech mischief, tips, and questionable metaphors.

---

# Art Prompt (Impressionism):

A shimmering riverside scene painted with soft, luminous strokes, capturing dappled sunlight dancing across rippling water. Clusters of foliage glow in gentle greens and yellows, broken into tiny, vibrant color notes that shimmer like mosaic reflections. A hazy sky melts into the horizon in pale lavender and warm peach, with delicate brushwork evoking the breezy serenity of a quiet afternoon along a peaceful shoreline. The entire composition radiates a lively, pointillist sparkle, blending atmosphere and light into a dreamy, harmonious landscape.

---

# [Video Prompt:](https://www.tiktok.com/@davelumai/video/7576257030449614110)

Begin with a slow, gliding shot over shimmering water, each ripple catching flecks of pastel light. Transition into gentle push-ins on clusters of glowing foliage, with tiny dots and strokes appearing to assemble themselves in real time. Add drifting particles of soft color that float through the frame as if brushed on by invisible hands. Slowly tilt upward into a hazy lavender-peach sky that blooms into a full, vibrant panorama. Finish with a smooth pullback that reveals the entire riverside scene forming organically, as if the painting is coming alive stroke by shimmering stroke.

---

## Song Suggestions

Pair the video with:

* **Cherry-coloured Funk – Cocteau Twins**
* **Coffee – beabadoobee**


---

Drop your questions, your disasters, your triumphs, or your “I accidentally committed an entire VM image” stories below. And hit follow for more adventures in art, tech, and occasionally responsible Git usage.



        <blockquote class="tiktok-embed" cite="https://www.tiktok.com/@davelumai" data-unique-id="davelumai" data-embed-type="creator" style="max-width: 780px; min-width: 288px;" > <section> <a target="_blank" href="https://www.tiktok.com/@davelumai?refer=creator_embed">@davelumai</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
