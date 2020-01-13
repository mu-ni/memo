S – Situation - background info
T – Task - what you had to do
A – Activity - what you did - this should be the longest part of the answer
R – Results - positive; quantifiable; what you learned; what you would do differently next time
TODO：多几个例子

FEDB
delta-compute
workflow research, kaggle
UT
useless map keys

i18n, 2 set of mapping
jboss -> spring-boot, new technology
improve performance: get metadata from zk -> keep in memory
micro-service -> spring-cloud
todo: avro & protobuf

Leadership Principles
We use our Leadership Principles every day, whether we're discussing ideas for new projects or deciding on the best approach to solving a problem. It is just one of the things that makes Amazon peculiar.

1. Customer Obsession（顾客至上，从客户角度出发获取信任，关注竞争者，但是更关心客户）
Leaders start with the customer and work backwards. They work vigorously to earn and keep customer trust. Although leaders pay attention to competitors, they obsess over customers.
- Walk us through a time when you helped a customer through a difficult progress
  S - hard to deliver model, translate/develop ML application
      2 main projects in our team, FEQL&RTIDB
  T - FEDB, system based on FE&DB, simplify ML workflow
  A - from scratch, manage data, support both batch&realtime
  R - 40% delivery projects are using FEDB, Patent

- Who was your most difficult customer?
  no. data scientist and delivery team
  S - input map with many useless keys, hard to understand initially
  T - clarity requirements before starting
  A - I've been to customers' office several times, DT based in there
      try to understand real customers' requirements
  R - their requirements are more reasonable, more close to customer

- Give me an example of a time when you did not meet a client’s expectation. What happened, and how did you attempt to rectify the situation?
  Never, before the starting, clarify the requirement.
  really understand, without misunderstanding
  learned from my past experience. Do not just image what it should be, but discuss
  review the progress everyweek/everyday
  Make sure on the correct way, or change the direction as early as possible

- When you’re working with a large number of customers, it’s tricky to deliver excellent service to them all. How do you go about prioritizing your customers’ needs?
  Pareto principle(80/20 rule) - for many events, about 80% of the results come from 20% of the decisions
  Can not satisfy all, just satisfy the most important requirements
  requirements from data scientist and delivery team, list the priority
  same priority, first do task with less risks
  develop -> main function first, then user experience improvement
             less risks first, complex task later, not block QA test
  major bug, block normal workflow, fix firstly
  potential risks, make DB unsafe, fix secondly
  user experience, todo list, fix it later
  Don't need to build a perfect product at the beginning, a good product should keep iterating

2. Ownership（目光长远，不为短期结果牺牲长期价值，从不说”那不是我的工作”）
Leaders are owners. They think long term and don’t sacrifice long-term value for short-term results. They act on behalf of the entire company, beyond just their own team. They never say “that’s not my job."
- Tell me about a time when you had to leave a task unfinished.
  This rarely happens
  S - re-organization
  T - transfer project to SH
  A - arrange several workshop, IM chat group, make sure they are totally understand
  R - currently managed well

- Tell me about a time when you had to work on a project with unclear responsibilities.
  S - latest project, delta compute, compute once -> continious computation, data generated continuously
  T - 4 people, cooperated to develop
      base in both BJ and SH, poor communication, waiting for each other
  A - propose - daily meeting, 5min
  R - released on time

- Tell me a challenge you had where the best way forward was not clear cut. How did you decide what to do?
  S - research is a part of my work
  T - make ML workflow simple, more engineers can develop AI applications
  A - kaggle, dataset&competitions, collect information from delivery team
  R - Logistic regression&Random forest, gained a lot of positive feedback

- Give me an example of something you tried to accomplish/took a risk but failed
- Tell me about a time when you took a calculated risk.
  S - not for internal use only, but attract more external developers
  T - make a standard for AI application development workflow
      Last quarter, planed to attract at least 100 developers to use our system
  A - But, many internal projects need to be supported, higher priority
      don't have enough energy to promote and operate our product
      projects we need to supported are more than our expection
  R - it is a pity, we didn't achieve it, hope do it later

- Give me an example of a time when you showed initiative.
  FEQL: like SQL for both batch&realtime feature computing
  RTIDB: time sensitive scenariao
  S - fedb, based on FEQL & RTIDB
  T - promote fedb to DS DT, simplify the workflow
  A - participated in their workshop, requirements & advices
  R - reduce 60% of workload, more customers

3. Invent and Simplify（创新的发明，寻找简化方法。从任何地方寻找新的想法。在做新的事情时，可以接受一段时间内存在误解）
Leaders expect and require innovation and invention from their teams and always find ways to simplify. They are externally aware, look for new ideas from everywhere, and are not limited by “not invented here." As we do new things, we accept that we may be misunderstood for long periods of time.
- Tell me about a time when you gave a simple solution to a complex problem.
  1. lombok, annotation, fluent style, simple and clear
  2. zookeeper retry & timeout: easy to make mistakes -> curator
  3. http -> rpc, grpc/brpc, protobuf

- Tell me about a time when you invented something
- Tell me a time when you created an innovative product
- Most challenging project?
  that is exactly my current project, major contributor
  I started my current project one year ago from scratch
  idea from delivery team
  last 6 months, only one developer(me), recently, aother 2 developers joined
  notice that it is hard for delivery team to deliver a model to customer smoothly
  pyspark - java, cost at least one week for development, with many errors
  We want to develop a system that make model on production without any modification
  we schedule some workshops for sharing our ideas with data scientist and collect opinions from them
  Keep constraints - can not develop a product perfectly at the first version - keep iteration


4. Are Right, A Lot（领导者有更强的判断力和直觉，接受不同的观点）
Leaders are right a lot. They have strong judgment and good instincts. They seek diverse perspectives and work to disconfirm their beliefs.
- tell me about a time when you are wrong
  Actually, I didn't make serious mistake in my work, But I have learned some lessons
  S - just want to fix the specific bug asap, old bugs appear again and again
      hard to fix a bug without introduce new bugs
  T - avoid already fixed bugs happening again
  A - UT, every function should have its own ut before merge to the main branch
  R - With complete UT, fix a bug, don't afraid at all. UT give us enough confidence
      biggest lesson I've learned during my previous work

- tell me about a time when you had to work with incomplete data or information
- Tell me about a time where you overcame an obstacle and delivered results.
- Obstacles met during a project
  S - hard to develop AI application, don't know how to start
  T - make ML workflow more simple for developers
  A - totally new to it, not enough info about it
      kaggle dataset, join competition
  R - use research result in my current project, with clear workflow, easy to develop
      don't need to care about the details, just focus on their own business logic


5. Learn and Be Curious（保持学习，提升自己，对新事物好奇，乐于探索）
Leaders are never done learning and always seek to improve themselves. They are curious about new possibilities and act to explore them.
- How do you find the time to stay inspired, acquire new knowledge, innovate in your work?
  S - innovation is a part of my work, IEG- innovating engineering group
  A - logical regression/random forest
      async call, completableFuture(jdk8)
      redis
      CICD embeded with gitlab
      high quality/performance code


6. //Hire and Develop the Best（善于发现人才，指导他人）
Leaders raise the performance bar with every hire and promotion. They recognize exceptional talent, and willingly move them throughout the organization. Leaders develop leaders and take seriously their role in coaching others. We work on behalf of our people to invent mechanisms for development like Career Choice.
- Tell me about a time when you mentored/coached someone.
  S - one fresh-graduate colleague in our team, I am his mentor
      code quality is not good enough, demo ok, not production.
      variable naming, all codes in same function, no UT
  A - code review & recommand some useful plugins for him, lombok
  R - his code looks better now

- Sometimes when teammates are not "qualified"
- Tell me about a time when you had to deal with a poor performer on your team.
  I don't think anyone is not qualified, just because this task is not suitable for him
  Try to understand his interests and the fields he is good at
  not just coding without any preparation
  Everyone has his own strengths and weak points, put him in the suitable place

- Give me an example of a time when you motivated others.激发灵感，激发动力
  not by myself, motivated each other
  workshop for sharing ideas, daily meeting
  most of good ideas come from brainstrom

7. Insist on the Highest Standards（坚持最高标准，交付高质量产品）
Leaders have relentlessly high standards — many people may think these standards are unreasonably high. Leaders are continually raising the bar and drive their teams to deliver high quality products, services, and processes. Leaders ensure that defects do not get sent down the line and that problems are fixed so they stay fixed.
- Tell me about a time when you could have stopped working but persisted.
  workable -> improve performance
  1. Access zk node -> keep in memory, init form zk, reduce zk access, reduce the stress of zk
  2. Async call, completableFuture, jdk8

- Tell me about a time when you couldn’t meet your own expectations on a project.
  time or quality?
  time - internship, afraid to talk with others, missed deadline
  quality - depends on time. if urgent, delivery important than quality

- Tell me about a time when a team member didn’t meet your expectations on a project.
  progress or quality?
  no, keep in touch, follow his progress
  can't not finished is acceptable, re-calculate the workflow
  Not say cannot finish at the last minute

8. Think Big（大胆思考，激发成果）
Thinking small is a self-fulfilling prophecy. Leaders create and communicate a bold direction that inspires results. They think differently and look around corners for ways to serve customers.
- Tell me about a time when you proposed a new business.
  FEDB

- Tell me about your proudest professional achievement.
  FEDB, release to real-time prediction without any modification
  expose our abilities to more customers
  simplify the workflow, save a lot of time and resource
  already used in 60% of projects within delivery teams
  I felt a strong sense of success/I am so proud of it
  submit a patent about fedb

- Tell me about a time when you went way beyond the scope of the project and delivered.
  improve performance, async
  Not limited by customers' requirements, sometimes customers are not clear what they want
  Sometimes the progress is complex, but they are already used to this progress
  We will give them one more choice and let them know there is another progress which is more simple and clear
  try to think from the customers' point of view, and dig into their requirements
  Not just, my boss ask me to use it, But, it is really useful so I would like to use it

9. Bias for Action（速度至关重要，决定和行动有时可逆，做好风险评估）
Speed matters in business. Many decisions and actions are reversible and do not need extensive study. We value calculated risk taking.
- Describe how you would handle a busy situation where three people are waiting for help from you.
  list the priority, calcutate risk in advance, try to minimize the risk
  If someone is waiting for me, I'll do it first, try not to block others work
  IM chat group, help each other

- Describe a time when you saw some problem and took the initiative to correct it rather than waiting for someone else to do it.
  try to collection feedback from users, I am the owner of this project
  don't think just start doing by myslef is a good choice, maybe it is by design
  should discuss first, if really necessary and I’d like to fix this problem
  QPS is hight, fix code not thread safe, add locks


- Tell me about a time you needed to get information from someone who wasn’t very responsive. What did you do?
  Maybe he is busy in sth, do not disturb his progress
  prepare enough by myself before, do not ask stupid questions
  don't just wait for his response, book a short time of him, 10mins, for asking questions


10. //Frugality（争取事半功倍）
Accomplish more with less. Constraints breed resourcefulness, self-sufficiency, and invention. There are no extra points for growing headcount, budget size, or fixed expense.
- Tell me about a time where you thought of a clever new way to save money for the company.
  fedb, online-offline consistency

- Tell me about a time when you delegated a project effectively.高效上线项目
  Assign tasks properly
  communication is very important
  review progress everyday
  delta-compute, not finished yet, but milestones
  finish as planed, no delay, no major bugs -> is success

11. Earn Trust（获取信任，乐于倾听，尊重他人，多从自身找原因）
Leaders listen attentively, speak candidly, and treat others respectfully. They are vocally self-critical, even when doing so is awkward or embarrassing. Leaders do not believe their or their team’s body odor smells of perfume. They benchmark themselves and their teams against the best.
- Tell me a time when you earned trust of a group.
  joined this team firstly, we don't know each others background
  propose monthly knowledge sharing workshop, know others technical background soon, earn trust from each other

12. Dive Deep（关注细节，及时review，及早发现）
Leaders operate at all levels, stay connected to the details, audit frequently, and are skeptical when metrics and anecdote differ. No task is beneath them.
- Tell me about a time when you had to dive deep into the data and the results you achieved.
  ML workflow research, not much tutorials about this
  kaggle, dataset, participated in competations
  product - fedb, every engineer can build an AI application in one day

- A time working on a project and the results exceeded the goals
- Give me two examples of when you did more than what was required in any job experience.
  Current project, from scratch, just an innovation
  innovation project, 50 percent chance to fail. But luckily, we succeed/səkˈsiːd/
  Help our data scientist and delivery team -> reduce time to deliver
  use same code(SQL) for batch-compute and realtime-compute
  firstly just want to support 1 project, but now 5,6 projects use fedb


13. Have Backbone; Disagree and Commit（敢于挑战权威，敢于对自己的决策负责）
Leaders are obligated to respectfully challenge decisions when they disagree, even when doing so is uncomfortable or exhausting. Leaders have conviction and are tenacious. They do not compromise for the sake of social cohesion. Once a decision is determined, they commit wholly.
- Tell me about the most difficult interaction互动 you had at work.
- Tell me about a time when you did not accept the status quo现状.
  previous work, after reorganization, colleagues don't accept new technologies
  I try to share latest knowledge with them but it seems they are not interested
  I discuss my ideas with my manager, he support me a lot
  We can use popular technologies in new project(jboss - spring-boot)

- Tell me about a time when you had to step up and disagree with a team members approach.
  1. framework, over-designed - native code, not import unnecessary dependencies, not make project complicates
     cron job, expression or framework
  2. db denormalization, get result quickly - redundant data
     user's courses, join search or just save to user table as a list

- If your direct manager was instructing you to do something you disagreed with, how would you handle it?
  Although most of time he is correct
  I will discuss with him firstly before I staring to do
  Normally both of us are correct, Just because we have different points of view
  It is normal that people have disagreements
  the most important thing is listen carefully to his opinions and share my opinions with him
  Because our goals are the same, and I am sure we will reach an agreement on at least one point
  We should start from this point and try to reach the final agreement

14. Deliver Results（按时交付高质量产品，遇到挫折挺身而出，对产品有追求，不满足于现状）
Leaders focus on the key inputs for their business and deliver them with the right quality and in a timely fashion. Despite setbacks, they rise to the occasion and never settle.
- What is the most difficult situation you have ever faced in your life? How did you handle it?
  fix a simple bug, 2 weeks, UT

- By providing an example, tell me when you have had to handle a variety of assignments任务. Describe the results.
  list priority
  pareto principle
- Tell me about a time when you had to work with limited time or resources.
  ML workflow research, kaggle, data scientist

- Couldn’t finish tasks before deadline?
  Never happened in recent years
  When I did my internship 4 years ago. Can not estimate workload very well
  I was blocked, feel afraid to ask someone for help, even didn't tell my boss
  When I didn't finish my task in deadline, I realized that this is not correct
  Now, daily work plan and todo list
  I can estimate the workload very well
  This situation will never happen again
  if really, tell PM as early as possible, reschedule the workload
