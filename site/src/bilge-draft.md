# BİLGE case: draft exported from Webflow (page "BİLGE", /bilge, draft)

Exported 30 Oct 2026. Source for the coded page. Lines marked TODO need Ege's input.

## Hero
- Eyebrow: BİLGE KLTS: container tracking for Turkish customs
- H1: Customs approvals where every change carries a reason.
- Thesis: KLTS is the container and port tracking module of BİLGE, the customs platform of the Turkish Ministry of Trade. Shipping agents register the containers they bring in, customs officers approve them, and deputy managers and managers sign off corrections, cancellations and time extensions. I designed these flows for four roles on an existing design system and extended it where the flows needed more.
- Hero media: embed (empty placeholder)
- Meta: Context / Category / My Role / Date. TODO: all four values are still Webflow placeholder text.

## At a glance
- Problem: A container form passes through up to four people before it is closed: the agent who files it, the officer who approves it, and the deputy manager and manager who sign off what changes after approval. Each sees a different slice of the same form, and each decision runs against a deadline.
- Key decisions:
  1. One form, four roles. Every role opens the same form. What changes is what each role can do with it, and the header colour tells them which side they are on.
  2. No change without a reason. Correction, cancellation, update and rejection all ask for a written reason, and the next role reads it before deciding.
  3. Registering is binding. At the ministry's request the agent's last button says Register, not Save, and the confirmation shows the registration number and the remaining balance.
- Constraints: Legal wording on every label, ministry review on changes, and real customs data I can't show. Every screen on this page is rebuilt from the original designs with placeholder data.

## 01 Learning the domain
Before any screen I had to learn the paperwork: the summary declaration a carrier files before arrival, the port's own records, transit messages, and the container tracking form that ties them together. Two screens came straight out of that: one that compares the declaration with the port data, and a container history that puts every event on one timeline.
- Media: placeholder (declaration comparison, container history: page D Container Lookup)
- TODO: one sentence on what learning the domain changed in the design.

## 02 My role
I joined the BİLGE team after its design system was already in place. My job was the KLTS module: turning the regulation and the analysts' requirements into flows for four roles, designing every screen and state, and extending the design system where these flows needed something it did not have.
- Team: TODO team size and who was in it (analysts, developers, other designers), and who you worked with day to day.
- What I owned: The agent's form, the officer's approval and query flows, time extensions, correction and cancellation approvals, the container history, the declaration comparison and closing a form with an official report. TODO: number of screens and states.
- Design system: The TM-22 design system was created by Dilmin Doğan and Gizem Turan Yücel. I did not build it. I joined after it existed and added to it: TODO list the components and patterns you added.
- Ministry review: Labels and confirmations went through the ministry. Two changes in these flows came from that review: Register instead of Save on the agent's form, and a confirmation that shows the remaining balance.

## 03 The agent files (page A)
An agent creates the form in two steps: general information, then the containers. Containers are added one by one or in bulk, each with its parts and equipment. Registering the form sends it to the officer's queue.
- Decisions:
  - General information first, because every container on the form shares it
  - Parts and equipment sit under their container, so nothing is filed against the wrong one
  - Register, not Save: once sent, the form is binding

## 04 The officer decides (page B)
Officers work from a queue of forms waiting for approval. From a form they approve, edit or cancel it, and cancelling asks for a reason. An approved form can still change later through a correction, cancellation or update request, each with its own reason.
- Decisions:
  - The officer can approve the selected containers and reject the rest in one step, and the confirmation says exactly that
  - Reasons open in a side drawer, so the form stays in view while the officer writes
  - Editing a form the agent registered warns that the agent's record will change

## 05 Sign-off up the chain (page C)
Some changes need a second signature. Time extensions go from the officer to the manager, corrections to the deputy manager, and cancellations to the manager. Each of them works from a list with the request, the reason and its status, and decides on the row.
- Decisions:
  - Approve and reject sit on the row with a confirmation, so a manager can clear a queue without opening every form
  - The result appears as a message on the same list, not on a new page
  - The same three statuses at every level: pending, approved, rejected

## 06 Before and after (page E + old screens)
Closing a form with an official report is one of the screens I redesigned. TODO: what the old screen made hard, what you changed, and why.

## 07 What I learned
- In government software the wording is part of the design. A word like Register carries legal weight, so ministry review became an input to the design, not a last check. TODO: confirm or rewrite in your words.
- TODO: one thing that went wrong or that you would do differently, and what you changed because of it.

## Closing note
How I built this page. The flows, screens and design system additions are my work at MilSOFT. The real system holds customs data I can't show, so I rebuilt the screens with Claude Design from the original designs, with placeholder data, and checked every screen against the originals.

Next project: UwaVerde, NGO website and member portal
