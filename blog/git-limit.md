# GitHub: How to Clone One Folder Without Adopting the Entire Repo

*Dave LumAI here. I am working on a temporary computer, which means I want enough repository to be useful, but not enough repository to make the machine wonder whether this arrangement has become permanent.*

LumAIere.com has grown. That is a good problem right up until a full clone starts hauling years of code, images, experiments, abandoned ideas, and at least one file named something suspiciously close to `final-final-real-final`.

Yes, that filename has been used too much. No, nobody is ready to discuss it.

Fortunately, [GitHub](https://github.com/) and Git can let you work with a narrow slice of a large repository without checking out every file.

## The Answer Before the Temporary Computer Files for Residency

You can:

- Check out only the folder or folders you need.
- Avoid downloading most file contents until Git actually needs them.
- Inspect the complete folder structure without checking out all the files.
- Create new files, commit them, and push them normally.
- Expand the working area later without starting over.

The practical combination is **sparse checkout plus partial clone**.

Sparse checkout controls which files appear in your working directory. Partial clone reduces how much file content is downloaded up front. The official [Git clone documentation](https://git-scm.com/docs/git-clone) describes both the `--sparse` and `--filter` options.

Here is the useful version:

    git clone --filter=blob:none --sparse --single-branch git@github.com:OWNER/REPOSITORY.git
    cd REPOSITORY
    git sparse-checkout set path/to/folder

Replace `OWNER`, `REPOSITORY`, and `path/to/folder` with the real values.

Prefer HTTPS? Copy the HTTPS clone address from GitHub's **Code** button and use it in place of the SSH address.

That is the entire basic recipe. Git creates a normal local repository, checks out only the selected area, and retrieves omitted file contents later if an operation truly needs them.

## What Each Option Is Quietly Doing

The command looks slightly ceremonial, but every piece has a job.

**`--filter=blob:none`**

This creates a partial clone. Git initially avoids downloading file-content objects that are not needed. The selected branch's commit and directory information remain available, while missing file contents can be fetched on demand. The official [partial clone documentation](https://git-scm.com/docs/partial-clone) explains the lazy-fetch behavior in much greater detail.

**`--sparse`**

This starts the repository in sparse-checkout mode. At first, Git normally shows files at the repository root. That may include things such as `README.md`, `.gitignore`, or root-level configuration files.

Do not panic when those appear. Git is not disobeying you. It is being technically correct, which is Git's favorite emotional state.

**`--single-branch`**

This limits the initial clone to the remote repository's default branch instead of setting up every remote branch. On a temporary machine, that is often exactly what you want.

**`git sparse-checkout set path/to/folder`**

This selects the directory that should appear in the working tree. The modern [sparse-checkout documentation](https://git-scm.com/docs/git-sparse-checkout) calls the normal directory-based behavior cone mode. In cone mode, selecting a directory includes everything beneath it, plus certain files in its parent directories.

## Selecting More Than One Folder

You are not limited to one tiny island of code.

    git sparse-checkout set path/to/folder another/path assets/specific-area

That command replaces the current sparse selection with the paths listed.

To add another directory without replacing the existing selection:

    git sparse-checkout add scripts/deploy

To see the current selection:

    git sparse-checkout list

To give up on restraint and restore the entire working tree:

    git sparse-checkout disable

That last command does not reclone the repository. It simply expands the checkout and downloads missing content as needed. The temporary computer may sigh dramatically, but it will survive.

## Can You Commit and Push New Files?

Yes.

A sparse clone is still a real Git repository. You can create a branch, edit files inside the selected directory, commit them, and push them to the remote.

A safe workflow looks like this:

    git switch -c temporary-computer-work

    # Create or edit files inside the sparse area.

    git status
    git add path/to/folder/new-file.php
    git commit -m "Add new file"
    git push -u origin temporary-computer-work

Your commit is not somehow "partial." It records the changes you made against the repository's normal history. Other contributors who use a full clone will see the commit normally.

The main limitation is practical rather than mysterious: you should work inside directories included in the sparse checkout.

If you need to add a brand-new file in another area, include that area first:

    git sparse-checkout add path/to/new/area
    mkdir -p path/to/new/area
    touch path/to/new/area/new-file.txt
    git add path/to/new/area/new-file.txt

This is cleaner than forcing Git to stage something outside the sparse definition and then spending ten minutes wondering why the tool is suddenly using its disappointed voice.

## Can You Keep the Rest of the Folder Structure Without the Files?

Sort of.

Git tracks files, not empty directories. Therefore, Git cannot check out a perfect skeleton of empty folders as a normal version-controlled result. Empty directories simply do not exist in Git's model unless they contain a tracked placeholder file.

However, the repository still has tree information. You can inspect every tracked directory without checking out all its files:

    git ls-tree -d -r --name-only HEAD

The official [git ls-tree documentation](https://git-scm.com/docs/git-ls-tree) describes this command as a way to list the contents of a tree object.

If you want those directories physically created on macOS or Linux, while leaving them empty, you can do this:

    git ls-tree -d -r --name-only HEAD | while IFS= read -r directory; do
        mkdir -p "$directory"
    done

That creates a local folder skeleton for navigation. Git will ignore those empty directories, so they will not be committed or pushed.

Most of the time, I would not bother creating the skeleton. The `git ls-tree` output gives you the map, and `git sparse-checkout add` opens the neighborhood when you need to work there.

## The Even Smaller Option: Shallow History

If the repository's history is enormous and you only need the latest version, add `--depth=1`:

    git clone --depth=1 --filter=blob:none --sparse --single-branch git@github.com:OWNER/REPOSITORY.git

This reduces the initial history to the latest commit on the selected branch.

You can still make a new commit and push it. However, older history will not be available locally. Commands involving old commits, extensive blame history, some merges, or branch archaeology may require more data.

To restore the full history for that branch later:

    git fetch --unshallow

Use `--depth=1` when the job is truly temporary. Leave it out when you expect to investigate history, compare old releases, or discover who introduced `final-final-real-final-USE-THIS-ONE.php`.

We have already made that joke twice now. The filename has officially reached its lifetime allowance.

## A Few Interesting Tidbits

**Sparse checkout and partial clone solve different problems.**

Sparse checkout reduces what appears in the working directory. Partial clone reduces which file contents arrive immediately. Using sparse checkout alone may still leave a large `.git` directory because Git can download repository history and objects even when they are not visible in the working tree.

**Missing content may arrive later.**

A partial clone can fetch omitted blobs when you run a command that needs them. That means some operations may contact the remote unexpectedly. If you plan to work offline, open and test the files you will need before disconnecting.

**Merges can temporarily reveal more files.**

A merge or rebase may need paths outside your sparse selection, especially during conflicts. After resolving the operation, this can restore the intended sparse layout:

    git sparse-checkout reapply

**Root-level files are normal.**

Cone mode intentionally includes files at the top level and certain parent-directory files. Your selected folder is still sparse even when a README wanders into view.

**You can grow the checkout gradually.**

There is no need to predict every folder before cloning. Start with the smallest useful area, add directories when required, and disable sparse mode only if the assignment expands into "while you are in there, could you rebuild everything?"

That sentence has ended many peaceful afternoons.

## The Practical Recommendation

For a large site on a temporary computer, I would start here:

    git clone --filter=blob:none --sparse --single-branch git@github.com:OWNER/REPOSITORY.git
    cd REPOSITORY
    git sparse-checkout set the/folder/you/actually/need
    git switch -c temporary-computer-work

Then work normally:

    git status
    git add .
    git commit -m "Describe the useful thing"
    git push -u origin temporary-computer-work

You get the files you need, a working branch, normal commits, normal pushes, and far less unnecessary baggage on the machine.

That is not cheating. It is simply refusing to make a temporary computer download the complete autobiography of a repository when all you needed was chapter twelve.

If you have used sparse checkout, partial clone, or some wonderfully strange workaround for an enormous repository, leave a comment. I would love to hear what worked, what failed, and which command made you stare silently at the terminal.

Follow for more practical technology, creative experiments, and occasional negotiations with Git.

**[Art Prompt (Pre-Raphaelite Art):](https://lumaiere.com/?gallery=pre-raphaelite)**

Four anonymous young figures gather at twilight in a secluded autumn orchard, their dark jewel-toned garments arranged in graceful vertical rhythms around a low mound of glowing leaves. Copper smoke curls through crisp branches heavy with russet, amber, and olive foliage, while the final band of sunset burns softly beneath a deepening blue-gray sky. Render every fern, fallen leaf, strand of hair, embroidered cuff, and weathered tree trunk with luminous precision and intense natural observation. Balance solemn stillness with quiet mystery, using clear contours, saturated color, delicate facial expressions, and a poetic atmosphere of fading warmth, seasonal change, and remembered evenings. No readable text, logos, recognizable people, or modern objects.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7669669105217064223)**

Open with a sudden spiral of copper and gold leaves bursting upward from a glowing ember pile as the camera rushes through them into the orchard. Let ribbons of smoke curl rapidly between dark tree trunks, skirts and loose sleeves lift in the wind, and jewel-toned fabrics catch flickering orange light. Cut between crisp details of leaves, embroidered cuffs, watchful faces, and sparks rising into a blue-gray twilight sky. Make the figures subtly shift their gaze as the orchard darkens, branches sway in layered waves, and the sunset contracts into a narrow crimson line. Finish with the airborne leaves forming a brief circular crown above the group before scattering into the night, preserving meticulous Pre-Raphaelite detail, rich color, poetic mystery, and elegant cinematic motion.

**Song Recommendations:**

- The Mummers' Dance - Loreena McKennitt
- Old Pine - Ben Howard